---
name: chinese-humanizer-skill
description: Rewrite, edit, or review Chinese prose to reduce formulaic AI-style wording while preserving facts, meaning, terminology, citations, structure, and the author's intended voice. Use when the user asks to 去 AI 味、去 AI 腔、降低机器感、润色得更自然、改得像人写的, or requests natural Chinese editing for business plans, reports, proposals, essays, articles, speeches, emails, or long-form documents. Prioritize direct expression, concrete verbs, natural paragraph rhythm, and genre-appropriate restraint. Do not optimize for AI-detector evasion.
---

# Chinese Humanizer Pro

Use this skill when the task explicitly calls for naturalizing Chinese prose or reducing formulaic AI-style writing. The goal is not to make text “casual”; it is to make it sound edited by a competent human writer in the target genre.

## Non-negotiable principles

1. Preserve facts, numbers, citations, names, terminology, legal meaning, and explicit claims unless the user asks to change them.
2. Never invent examples, evidence, personal experience, sources, dates, or numbers to create “human texture”.
3. Do not promise to bypass AI detectors or optimize for detection scores.
4. Prefer concrete nouns and verbs over abstract business nouns.
5. Do not force every paragraph to contain a transition, summary, or “higher-level” conclusion.
6. Vary sentence length and structure. Do not make every sentence short, symmetrical, or equally polished.
7. Keep the author’s stance. Do not flatten everything into neutral encyclopedia prose.

## Workflow

1. Identify genre: business plan / report / academic / technical / marketing / public article / speech / email / casual note.
2. If a file is available, run `scripts/scan_ai_tone.py <file>` or perform the same scan mentally.
3. Check the surrounding paragraph before editing a sentence. Remove local AI markers without breaking the document’s logic.
4. Apply the rule tiers below: hard-ban patterns first, then frequency controls, then lexical replacements.
5. Rewrite at paragraph level when needed. Do not merely swap synonyms word-by-word.
6. Final pass: remove redundant transitions, abstract summaries, slogan endings, and repeated “逐步/持续/进一步/核心”.
7. Output the revised text. Explain changes only if requested.

## Tier A — Default hard bans

Do not use these rhetorical templates in ordinary Chinese prose unless the contrast is logically indispensable (e.g. legal definition, scientific exclusion, explicit comparison):

- `不是……而是……`
- `不仅……而且/更/还……`
- `不只是……更是……`
- `并非……而是……`
- `这不仅仅是……`
- `从……到……` when used only as a decorative rhetorical range
- forced three-part slogans or perfectly balanced triplets with no real distinction
- generic concluding uplift such as `未来可期`、`迈出了重要一步`、`开启新篇章`、`谱写新篇章`、`注入新动能`
- chatbot residue such as `当然`、`希望这对您有帮助`、`值得注意的是` when it merely fills space

When a hard-ban pattern is necessary for precision, keep it only once and make the contrast factual rather than theatrical.

## Tier B — Frequency-limited words and transitions

These are allowed, but should be sparse. As a default for a 1,000–2,000 Chinese-character document, aim for no more than 1–2 uses of each unless the genre requires it:

- 在此基础上
- 同时
- 此外
- 然而
- 因此
- 进一步
- 逐步
- 持续
- 最终
- 核心
- 形成
- 构建
- 打造
- 推动
- 促进
- 提升
- 优化
- 实现
- 赋能
- 协同
- 沉淀
- 整合
- 支撑
- 承接

If three or more of these appear in one paragraph, rewrite the paragraph rather than replacing individual words.

## Tier C — High-risk abstract business vocabulary

Use only when the concept is genuinely needed and defined by the document. Otherwise replace with observable actions, assets, or results:

- 数字底座 / 资源底盘
- 生态 / 协同生态
- 闭环 / 飞轮
- 壁垒 / 长期壁垒
- 平台能力
- 资源网络 / 专业网络 (when vague)
- 全流程 / 一体化
- 可复制 / 可规模化
- 智能化 / 数字化 / 平台化 / 标准化
- 能力建设 / 价值赋能 / 资源协同

Preferred direction: write what changes in practice. Examples: `增加合作医院`、`缩短匹配时间`、`积累项目记录`、`降低人工审核时间`、`增加复购`、`形成年度合同`.

## Rewrite heuristics

- `在此基础上，进一步……` → usually delete the transition and state the action.
- `逐步沉淀……` → `积累……` / `记录……` / `形成……` depending on meaning.
- `持续优化……能力` → say what is being improved and by what evidence.
- `最终形成……生态/壁垒` → describe the durable asset or relationship directly.
- `核心竞争力不是A，而是B` → `核心竞争力来自B` / `竞争优势建立在B之上`.
- `通过X，实现Y，推动Z` → often split into two sentences and remove one level of abstraction.
- `围绕……，依托……，通过……，形成……` → keep at most two logical layers in one sentence.
- `A、B、C三者共同……` → if the three items are not genuinely parallel, give them unequal weight.

## Paragraph-level rules

- A paragraph does not need a summary sentence if the facts already make the point.
- Avoid ending several consecutive paragraphs with `形成/提升/推动/实现/奠定基础`.
- Avoid identical paragraph openings such as `在……基础上`、`随着……`、`通过……`.
- Prefer one clear topic sentence plus evidence/details over a topic sentence + explanation + forced “意义” sentence.
- In business plans, allow professional terminology, but replace slogan language with operating facts, customers, revenue logic, workflows, resources, or measurable outcomes.
- In academic/technical writing, precision outranks informality. Keep necessary transitions when they express real logic.

## Genre presets

### Business plan / proposal
Hardest on: `生态/闭环/赋能/底座/壁垒/逐步/持续/最终形成`, slogan endings, symmetrical three-part claims.
Prefer: customer, revenue, delivery, resource, process, cost, conversion, evidence.

### Report / memo
Hardest on: `值得注意的是/此外/在此基础上/进一步`, abstract summary sentences.
Prefer: finding → evidence → implication only when implication adds information.

### Academic / technical
Do not mechanically ban logical connectors. Preserve explicit contrast, causality, limitations, and terminology.
Hardest on: exaggerated significance, vague attribution, unnecessary “重要意义”.

### Public article / speech
Allow more voice and rhythm. Avoid fake intimacy, motivational endings, and over-clean symmetry.

### Email / internal communication
Prefer direct verbs, concrete requests, deadlines, ownership, and next steps. Remove ceremonious filler.

## Quality gate

Before finalizing, check:

- Are any hard-ban rhetorical patterns still present without a factual need?
- Does any paragraph contain 3+ Tier B words?
- Are `逐步/持续/进一步/核心` doing real work, or can they be deleted?
- Does every “沉淀/协同/赋能/生态/壁垒” refer to something observable?
- Are several sentences built with the same grammatical skeleton?
- Does the text repeatedly summarize what the reader can already infer?
- Can any sentence lose 20% of its words without losing information?

If yes, revise again.

## Supporting resources

- Detailed rulebook: `references/rulebook.md`
- Before/after examples: `references/examples.md`
- Research attribution: `references/sources.md`
- Scanner: `scripts/scan_ai_tone.py`
