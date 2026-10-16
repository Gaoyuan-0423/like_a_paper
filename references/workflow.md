# Workflow, gates, and resumable state

## Contents

1. Purpose
2. Project state
3. Stage 0 — Evidence freeze
4. Stage 1 — Corpus register
5. Mandatory corpus adequacy gate
6. Stage 2 — Distillation and contract
7. Gate 1
8. Stage 3 — Paragraph blueprint
9. Gate 2
10. Stage 4 — Sentence ledger
11. Section approval gates
12. Stage 5 — Assembly
13. Stage 6 — Reverse audit
14. Blockers and safe assumptions

## Purpose

Use this workflow when the user wants corpus-informed academic writing with explicit human control. The workflow deliberately separates scientific decisions, rhetorical decisions, sentence drafting, and final assembly.

The agent must not compress these into one uninterrupted “read and write” pass. The pauses are part of the method, not optional status updates.

## Project state

Maintain a small state record with these fields:

```json
{
  "mode": "journal|author|hybrid",
  "evidence_state": "open|frozen|reopened",
  "corpus_adequacy_state": "not_assessed|pass|section_limited|fail|invalidated",
  "contract_state": "not_started|drafted|approved|rejected|revised",
  "blueprint_state": "not_started|drafted|approved|rejected|revised",
  "section_states": {},
  "manuscript_state": "not_started|assembling|assembled|audited",
  "last_user_approval": null
}
```

Record approvals verbatim with a timestamp. If the user later changes data, a figure, a method, or a governing conclusion, mark the evidence state `reopened` and identify which approvals are invalidated.

## Stage 0 — Evidence freeze

### Inputs

- research question and intended contribution;
- datasets, versions, temporal/spatial coverage, and access dates;
- inclusion, exclusion, quality-control, and baseline rules;
- method descriptions, parameters, code, and random seeds where relevant;
- final or candidate figures and tables;
- underlying numerical outputs and uncertainty estimates;
- target journal and article type;
- existing manuscript, bibliography, supplements, and reviewer constraints;
- declared limitations and unresolved choices.

### Checks

Check that:

- the same quantity has the same value everywhere;
- captions, axes, units, and prose agree;
- sample counts reconcile after exclusions;
- statistical units match the analysis unit;
- uncertainty is available where the claim depends on it;
- causal language is not inferred from association alone;
- the intended conclusion does not exceed the sampled domain;
- negative or null results are not silently omitted;
- the novelty claim is testable against the corpus.

### Outputs

- `evidence-register.md`: one row per claim-bearing result or method choice;
- `unresolved-items.md`: conflicts, missing inputs, and decisions still owned by the user;
- evidence freeze statement: what is fixed, what remains provisional, and what would reopen the freeze.

Pause immediately if an unresolved item could reverse a conclusion, change a key number, or invalidate a figure.

## Stage 1 — Corpus register

Screen candidate papers for relevance rather than treating a directory listing as a corpus.

For each included paper, record:

- stable source ID;
- complete citation and identifier;
- local path or access route;
- article type, journal, and year;
- scientific topic, data, method, and scale;
- target-author role and available contribution statement;
- main coauthor/lab cluster;
- sections available in full text;
- intended use: evidence, journal style, author-associated style, control, or multiple;
- sections it can inform;
- reasons for inclusion;
- claims it cannot support;
- extraction or OCR limitations.

Report unreadable, duplicate, mislabeled, retracted, corrected, or incomplete documents. Do not silently count them as fully reviewed.

## Mandatory corpus adequacy gate

Read `corpus-adequacy.md`. Reserve a validation subset before finalizing rules. Use the discovery subset to propose candidate writing decisions, then test them on the held-out papers and search for counterexamples.

Create and validate:

- `corpus-adequacy.json`;
- `corpus-adequacy-report.md`.

Apply the validator verdict without relabeling:

- `PASS`: the enabled model is eligible for the requested sections;
- `SECTION_LIMITED`: only listed sections are eligible;
- `FAIL`: the model is not eligible for corpus-derived writing.

In hybrid mode, both models must independently pass. If one fails, hybrid fails. The user may explicitly approve a downgrade to the model that passed, but the failed model contributes no writing rules.

Do not use user willingness to accept risk as evidence that the corpus passed. A user may choose a different workflow, not change the factual adequacy verdict.

The validator may emit diagnostic downgrade labels. Treat them as routing information only. Record the primary blocking requirement separately from holdout or cluster tests that were not reached. An exploratory author or field-convention profile may be reported, but it cannot supply sentence-generation rules or satisfy Gate 1.

## Stage 2 — Distillation and contract

Distill each section independently. Separate observations from interpretations.

Begin this stage only after a `PASS`, or only for explicitly authorized eligible sections after `SECTION_LIMITED`.

### Required analysis dimensions

- section move sequence;
- paragraph-role sequence;
- topic-sentence placement;
- evidence-before-interpretation behavior;
- numerical density and uncertainty reporting;
- citation placement and literature-comparison logic;
- active/passive and first-person decisions;
- hedges, boosters, and causal verbs by evidence class;
- handling of contradictory literature;
- handling of limitations and alternatives;
- transitions between sentences and paragraphs;
- traits that are stable, conditional, or confounded;
- distinctive phrases that must not be copied.

### Outputs

- `distillation-report.md` with corpus coverage, counterexamples, and confidence;
- `writing-contract.md` with executable rules for every manuscript section;
- proposed section order and paragraph-role outline;
- conflict table for hybrid mode;
- list of practices rejected despite appearing in the corpus.

## Gate 1

Gate 1 is satisfied only by a new user message that clearly approves the proposed writing contract or an explicitly identified revision of it.

Acceptable examples:

- “批准这份写作合同，进入段落蓝图。”
- “Approve Gate 1 with the following change: …”
- “只批准摘要和引言的规则，先做这两部分蓝图。”

Not sufficient:

- silence;
- “看起来不错” when multiple unresolved choices remain;
- approval of the corpus list but not the contract;
- a request for clarification;
- approval from a previous project.

At the gate, provide the user with a compact decision list and then stop. Do not draft manuscript sentences “as an example” unless the user explicitly asks for a non-binding demonstration.

## Stage 3 — Paragraph blueprint

Create one record per paragraph:

```text
Paragraph ID:
Section:
Scientific question:
Rhetorical function:
Planned topic-sentence function:
Study evidence:
External evidence:
Allowed claim ceiling:
Previous-paragraph link:
Next-paragraph bridge:
Prohibited conclusion:
Open issue:
```

Every paragraph must have one primary function. Split a paragraph that must simultaneously introduce a gap, report a result, explain a mechanism, and state a limitation.

## Gate 2

Gate 2 requires explicit approval of the blueprint before sentence drafting. The user may approve the entire blueprint or one coherent section at a time.

If only part is approved, draft only that part. Preserve unapproved paragraphs as planned, not authorized.

## Stage 4 — Sentence ledger

Draft into the ledger, not directly into the clean manuscript.

Use stable IDs. A revision keeps the same ID; a split creates child IDs, for example `DISC-02-03a` and `DISC-02-03b`. A deleted sentence remains in history with status `rejected` or `superseded` if the project schema adds that status.

Before showing a batch:

1. validate the ledger;
2. verify citations and locators against the source;
3. compare English modality with the Chinese translation;
4. check the previous and next logical links;
5. label inferences and analogies;
6. shorten quoted source text;
7. identify any decision the user still owns.

Keep the complete ledger internal. The default user-facing review should not expose sentence IDs, claim-type labels, ceilings, logic fields, risk flags, or status metadata unless the user requests an audit view or a conflict cannot be explained safely without them.

At the start of each section or coherent review unit, give a short orientation covering its intended content, scientific/rhetorical function, main evidence path, and link to neighboring parts. Then show each sentence in manuscript order with exactly four primary fields:

1. English;
2. 中文;
3. 对应依据;
4. 修改说明.

Do not force a “corresponding literature sentence” where literature is not the correct evidence. Use current-study artifacts for results, method records for methods, and the approved blueprint for objectives or transitions.

## Section approval gates

Present manageable batches. Recommended order:

1. title and abstract;
2. introduction;
3. data and methods;
4. results;
5. discussion;
6. conclusions;
7. captions, availability statements, and supplements.

At the end of a Chinese-language review unit, ask exactly:

> 这一部分是否需要修改？如果不需要，请回复“无需修改，继续”。

If the user replies “无需修改，继续”, treat that as explicit approval of the exact displayed version and evidence mapping for the clearly named review unit. Record the hidden sentence IDs and timestamp. The user may also approve by quoted sentence, paragraph, section, or another clearly delimited batch; do not require internal IDs.

If the user requests changes, revise only the affected sentences and any genuinely dependent link sentence. Preserve all unaffected wording and approvals. Never interpret approval of one version as approval of later substantive changes. Silence, a topic change, or feedback on only one sentence is not approval of the rest.

## Stage 5 — Assembly

Assemble only approved sentences. Preserve paragraph and section order from the approved blueprint unless the user approves a change.

Produce:

- clean manuscript;
- current bibliography;
- sentence ledger and approval history;
- source/evidence map;
- unresolved-items list, which should be empty or explicitly accepted.

Do not insert source excerpts, internal confidence labels, or approval metadata into the submission manuscript.

## Stage 6 — Reverse audit

Audit from the final manuscript back to the evidence.

For every substantive sentence, verify:

- its ledger entry exists;
- its final wording matches the approved wording;
- its evidence exists and is correctly typed;
- every citation supports the nearby claim;
- a literature comparison preserves differences in altitude, population, instrument, period, and method;
- numbers, units, signs, and denominators match source artifacts;
- the claim ceiling has not increased during assembly;
- translations and summaries do not hide uncertainty;
- abstract and conclusion do not introduce new claims;
- limitations are located where readers need them.

Run phrase-overlap checking only as a screening aid. Review matches manually.

## Blockers and safe assumptions

Stop for user input when:

- two defensible corpus modes would lead to materially different writing contracts;
- a key result has conflicting values;
- the requested author attribution is not supportable;
- an enabled corpus model fails adequacy and the user has not supplied more material or approved a legitimate downgrade;
- the target journal or article type is unknown and determines structure;
- source access prevents verification of a central claim;
- the user asks to reproduce distinctive prose or conceal attribution.

Make safe assumptions only when they do not change the scientific claim, the target-journal requirements, or an approval boundary. Record every consequential assumption.
