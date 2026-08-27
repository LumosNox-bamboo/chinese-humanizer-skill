#!/usr/bin/env python3
import re
import sys
from collections import Counter
from pathlib import Path

HARD_PATTERNS = {
    "不是…而是…": r"不是[^。！？；\n]{0,80}而是",
    "并非…而是…": r"并非[^。！？；\n]{0,80}而是",
    "不仅…而且/更/还…": r"不仅[^。！？；\n]{0,80}(?:而且|更|还)",
    "不只是…更是…": r"不只是[^。！？；\n]{0,80}更是",
    "这不仅仅是…": r"这不仅仅是",
}

LIMITED = [
    "在此基础上", "同时", "此外", "然而", "因此", "进一步", "逐步", "持续", "最终", "核心",
    "形成", "构建", "打造", "推动", "促进", "提升", "优化", "实现", "赋能", "协同", "沉淀", "整合", "支撑", "承接"
]

ABSTRACT = [
    "数字底座", "资源底盘", "协同生态", "生态", "闭环", "飞轮", "长期壁垒", "壁垒", "平台能力",
    "全流程", "一体化", "可复制", "可规模化", "智能化", "数字化", "平台化", "标准化"
]

COMBOS = [
    "逐步沉淀", "持续优化", "进一步提升", "最终形成", "构建闭环", "形成壁垒", "核心能力", "核心优势"
]

def read_text(path: Path) -> str:
    if path.suffix.lower() in {".txt", ".md", ".markdown"}:
        return path.read_text(encoding="utf-8")
    raise SystemExit("Scanner currently supports .txt/.md. Export document text first for other formats.")


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: scan_ai_tone.py <file.txt|file.md>")
    path = Path(sys.argv[1])
    text = read_text(path)
    chars = len(re.findall(r"[\u4e00-\u9fff]", text))
    print(f"Chinese chars: {chars}")

    print("\n[Hard-ban patterns]")
    hard_total = 0
    for name, pat in HARD_PATTERNS.items():
        hits = list(re.finditer(pat, text))
        if hits:
            hard_total += len(hits)
            print(f"- {name}: {len(hits)}")
            for m in hits[:5]:
                snippet = text[max(0,m.start()-18):min(len(text),m.end()+36)].replace("\n", " ")
                print(f"  · …{snippet}…")
    if not hard_total:
        print("- none")

    print("\n[Frequency-limited words]")
    counts = Counter({w: text.count(w) for w in LIMITED})
    scale = max(chars / 1500, 1)
    for w, n in counts.most_common():
        if n:
            flag = " !!" if n > max(2, round(2 * scale)) else ""
            print(f"- {w}: {n}{flag}")

    print("\n[High-risk abstract vocabulary]")
    found = [(w, text.count(w)) for w in ABSTRACT if text.count(w)]
    if found:
        for w, n in sorted(found, key=lambda x: -x[1]):
            print(f"- {w}: {n}")
    else:
        print("- none")

    print("\n[High-risk combinations]")
    found_combo = [(w, text.count(w)) for w in COMBOS if text.count(w)]
    if found_combo:
        for w, n in found_combo:
            print(f"- {w}: {n}")
    else:
        print("- none")

    score = hard_total * 4
    score += sum(max(0, n - max(2, round(2 * scale))) for n in counts.values())
    score += sum(n for _, n in found_combo) * 2
    print(f"\nHeuristic AI-tone risk score: {score} (lower is better; compare revisions, not authorship)")

if __name__ == "__main__":
    main()
