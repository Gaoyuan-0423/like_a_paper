# Bilingual sentence ledger

## Contents

1. Purpose
2. Canonical format
3. Required fields
4. Claim types
5. Evidence records
6. Logic links
7. Status and approval
8. Drafting sequence
9. Human-readable presentation
10. Examples

## Purpose

Use the sentence ledger as the controlled drafting surface. It is not the submission manuscript. It exposes meaning, evidence, inference strength, and local logic before prose is admitted into the clean paper.

Every candidate manuscript sentence receives a stable ID. The user may review the English sentence, Chinese meaning, evidence, source relationship, and paragraph connection without searching across a long draft.

## Canonical format

Store the machine-readable ledger as UTF-8 JSON Lines (`.jsonl`): one complete JSON object per line. Keep a rendered Markdown version for human review.

Use this top-level shape:

```json
{
  "sentence_id": "DISC-02-04",
  "section": "Discussion",
  "paragraph_id": "DISC-02",
  "function": "mechanism interpretation",
  "english": "...",
  "chinese": "...",
  "claim_type": "author_inference",
  "evidence": [],
  "claim_ceiling": "...",
  "previous_link": "...",
  "next_link": "...",
  "risk_flags": [],
  "status": "drafted",
  "approved_by": null,
  "approved_at": null,
  "notes": ""
}
```

## Required fields

### `sentence_id`

Use `SECTION-PP-SS`, for example:

- `ABST-01-03`;
- `INTRO-02-01`;
- `METHOD-04-05`;
- `RESULT-03-02`;
- `DISC-02-04`;
- `CONCL-01-02`.

Keep the ID through ordinary revisions. For a split, use suffixes such as `DISC-02-04a` and `DISC-02-04b` and retain the superseded record in version history.

### `section` and `paragraph_id`

Use the approved blueprint. Do not move a sentence into another paragraph silently.

### `function`

Describe what the sentence does, not its grammar. Examples:

- context;
- prior finding;
- gap;
- objective;
- method boundary;
- direct result;
- quantitative support;
- robustness;
- literature comparison;
- mechanism interpretation;
- alternative explanation;
- limitation;
- transition;
- implication.

### `english` and `chinese`

The English field is the candidate manuscript sentence. The Chinese field is a faithful semantic translation for user review, not a more confident or more fluent reinterpretation.

Preserve:

- positive/negative direction;
- units and numbers;
- modality;
- causal versus associative meaning;
- population, time, altitude, and spatial scope;
- exceptions and conditions.

### `claim_ceiling`

State the strongest conclusion permitted by the evidence. For a direct descriptive sentence, this can be a short boundary statement. For an inference, name the prohibited stronger claim.

### `risk_flags`

Use concise labels such as:

- `causal-overreach`;
- `scope-generalization`;
- `instrument-mismatch`;
- `population-mismatch`;
- `time-scale-mismatch`;
- `small-sample`;
- `selection-bias`;
- `translation-strength-shift`;
- `source-only-contextual`;
- `phrase-overlap`;
- `citation-needed`;
- `user-decision-needed`.

An empty list is allowed only after review.

## Claim types

Use one primary type:

### `external_fact`

A fact or prior finding about the field. Requires verified literature evidence with citation and locator.

### `study_result`

A result from the current study. Point to a figure, table, dataset, or analysis output. External literature is optional and normally belongs in a separate comparison sentence.

### `method`

A procedure, definition, instrument property, transformation, or analysis decision. Point to the method record, code, data documentation, or originating literature as applicable.

### `author_inference`

An interpretation or synthesis. Identify the current-study observation and relevant external or theoretical support. Mark alternative explanations and keep the verb below the claim ceiling.

### `limitation`

A boundary on interpretation or generalization. Point to the affected design, evidence gap, sampling constraint, validation result, or literature comparison.

### `objective`

A question, hypothesis, or stated task. Link it to the approved blueprint and gap rather than inventing a literature sentence that “supports” the author's intention.

### `transition`

A rhetorical connection. It normally requires no external citation. Describe what it closes and opens. Do not fabricate evidence to satisfy a citation quota.

## Evidence records

Each object in `evidence` uses:

```json
{
  "evidence_id": "LIT-YAMAZAKI-2024-A",
  "evidence_type": "literature",
  "citation": "Yamazaki et al. (2024)",
  "locator": "Discussion, paragraph 3; DOI: ...",
  "source_text_type": "excerpt",
  "source_text": "short source excerpt or faithful source note",
  "support_relation": "direct"
}
```

### Evidence types

- `literature`;
- `figure`;
- `table`;
- `analysis`;
- `dataset`;
- `method_record`;
- `code`;
- `journal_rule`;
- `user_decision`;
- `rhetorical`.

### Support relations

- `direct`: the source supports the stated proposition at the relevant scale;
- `partial`: the source supports only part of the sentence;
- `analogous`: the source supports a comparison under different conditions;
- `contextual`: the source supplies background but not the conclusion;
- `methodological`: the source supports a method or definition;
- `contrasting`: the source reports a result that differs and is being compared;
- `rhetorical`: the record documents a logic function rather than a scientific claim.

Never label analogous or contextual evidence as direct.

### Source text type

Use:

- `excerpt` for a short verbatim passage;
- `paraphrase` for a faithful note written in original words;
- `artifact_note` for a figure, analysis, dataset, code, or method locator.

Keep excerpts short. The validator warns when an English excerpt exceeds 25 words. A locator is still required for a paraphrase.

## Logic links

`previous_link` and `next_link` are required. They may contain `START` or `END` at a true boundary.

Good logic links state the relationship:

- “Quantifies the pattern introduced in RESULT-03-01.”
- “Closes the local-time comparison and motivates the altitude comparison in RESULT-04-01.”
- “Adds the principal alternative explanation to the mechanism proposed in DISC-02-03.”

Bad logic links merely say “continues the paragraph” or repeat the sentence.

## Status and approval

Allowed status values:

- `drafted`;
- `needs_revision`;
- `approved`;
- `rejected`.

When `status` is `approved`, require `approved_by` and an ISO 8601 `approved_at` timestamp. Approval applies to the exact wording and evidence mapping recorded at that time. A substantive revision returns the sentence to `needs_revision` or `drafted`.

## Drafting sequence

For each sentence:

1. identify the approved paragraph role;
2. select the scientific or rhetorical function;
3. state the claim in plain language;
4. map the correct evidence type;
5. set the claim ceiling;
6. draft original English below that ceiling;
7. translate faithfully into Chinese;
8. add a short source note and locator when literature is used;
9. explain the previous and next link;
10. add risks;
11. validate;
12. submit for user review.

Do not start from an attractive source sentence and mutate it into the manuscript sentence.

## Human-readable presentation

Render each sentence as a review card:

```text
DISC-02-04 | mechanism interpretation | drafted

English
...

中文
...

Claim type and ceiling
...

Evidence
- [direct/current analysis] ...
- [contextual/literature] ...

Logic
- Previous: ...
- Next: ...

Risks
- ...
```

When many sentences share the same source, keep each mapping explicit but avoid repeating a long excerpt. Refer to a stable evidence ID.

## Examples

### Current-study result

```json
{"sentence_id":"RESULT-03-02","section":"Results","paragraph_id":"RESULT-03","function":"quantitative support","english":"The median response peaked 6 h after the event onset.","chinese":"中位响应在事件开始后6小时达到峰值。","claim_type":"study_result","evidence":[{"evidence_id":"FIG-4B","evidence_type":"figure","citation":"","locator":"Figure 4b; analysis table timing_summary.csv, row median","source_text_type":"artifact_note","source_text":"Median peak lag = 6 h under the approved event definition.","support_relation":"direct"}],"claim_ceiling":"Describes the approved sample; does not establish a causal delay mechanism.","previous_link":"Quantifies the timing pattern introduced in RESULT-03-01.","next_link":"Prepares the subgroup contrast in RESULT-03-03.","risk_flags":[],"status":"drafted","approved_by":null,"approved_at":null,"notes":""}
```

### Interpretation with literature

```json
{"sentence_id":"DISC-02-04","section":"Discussion","paragraph_id":"DISC-02","function":"mechanism interpretation","english":"The delayed response is consistent with storm-driven circulation changes redistributing energy in the lower thermosphere.","chinese":"这种延迟响应与风暴驱动的环流变化在低热层重新分配能量的解释一致。","claim_type":"author_inference","evidence":[{"evidence_id":"ANALYSIS-LAG","evidence_type":"analysis","citation":"","locator":"Approved lag analysis; Figure 4","source_text_type":"artifact_note","source_text":"Response lag and confidence interval from the current study.","support_relation":"direct"},{"evidence_id":"LIT-A","evidence_type":"literature","citation":"Author et al. (Year)","locator":"Discussion, paragraph 2; DOI or stable identifier","source_text_type":"paraphrase","source_text":"The study links delayed lower-thermospheric temperature changes to circulation and vertical-motion responses.","support_relation":"contextual"}],"claim_ceiling":"Permits consistency, not causal identification; alternative transport and sampling explanations remain.","previous_link":"Interprets the lag quantified in the preceding sentence.","next_link":"Introduces why the available observations cannot distinguish the candidate mechanisms.","risk_flags":["causal-overreach"],"status":"drafted","approved_by":null,"approved_at":null,"notes":""}
```

### Transition

```json
{"sentence_id":"DISC-03-01","section":"Discussion","paragraph_id":"DISC-03","function":"transition","english":"This timing dependence motivates a separate examination of local-time structure.","chinese":"这种时间依赖性促使我们进一步单独考察地方时结构。","claim_type":"transition","evidence":[{"evidence_id":"BLUEPRINT-DISC-03","evidence_type":"rhetorical","citation":"","locator":"Approved paragraph blueprint DISC-02 to DISC-03","source_text_type":"artifact_note","source_text":"Move from timing to local-time structure.","support_relation":"rhetorical"}],"claim_ceiling":"Organizational transition only; does not claim a physical mechanism.","previous_link":"Closes the timing interpretation in DISC-02.","next_link":"Opens the local-time result comparison in DISC-03-02.","risk_flags":[],"status":"drafted","approved_by":null,"approved_at":null,"notes":""}
```
