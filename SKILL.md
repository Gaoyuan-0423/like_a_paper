---
name: like-a-paper
description: Evidence-traceable academic manuscript writing and revision that learns high-level writing decisions from a target-journal corpus, one author's cross-journal corpus, or both. Use when a user asks to study related papers before writing, require the literature corpus to pass adequacy and held-out stability standards, adapt a manuscript to a journal, distill an author's recurring argumentation patterns without copying their voice, freeze results and figures before drafting, require explicit human approval gates, build paragraph logic, or review every proposed sentence with a Chinese translation and a source/data evidence trail before assembling the final paper.
---

# Like a Paper

Build a manuscript from verified research evidence and a corpus-derived writing contract. Distill rhetorical decisions, not reusable prose. Keep every substantive claim traceable, stop at mandatory approval gates, and assemble the clean manuscript only from approved sentences.

## Non-negotiable rules

1. Preserve scientific truth, uncertainty, and user-owned results above stylistic resemblance.
2. Never claim that a multi-author paper reveals one author's personal voice. Call it an **author-associated corpus profile** unless authorship evidence supports a stronger attribution.
3. Do not imitate distinctive wording, signature phrases, or a living author's recognizable voice. Extract section structure, evidence sequencing, claim calibration, paragraph logic, and other high-level academic traits.
4. Write original prose. Use short source excerpts only for audit and always record a locator. Do not assemble text by synonym-swapping source sentences.
5. Distinguish external facts, study-specific results, methods, author inferences, limitations, and rhetorical transitions. They require different evidence.
6. Do not force an external citation onto a sentence supported by the user's figure, table, dataset, analysis, or method record. Do not fabricate a source for a transition sentence.
7. Preserve modality in translation: `may`, `suggest`, `support`, `indicate`, `demonstrate`, association, and causation are not interchangeable.
8. Stop at every mandatory gate. Silence, partial feedback, or approval of one item is not permission to continue.
9. Do not start corpus-derived writing until every enabled corpus model passes the adequacy gate for the requested sections. Paper count alone is not a pass.

## Start the task

At first invocation:

1. Explain the three modes in one short paragraph.
2. Infer a mode from the supplied materials when safe; otherwise ask the user to choose one.
3. Inspect available files before asking for information that can be discovered locally.
4. State that no manuscript prose will be drafted before the writing contract is explicitly approved.
5. Read [references/user-guide.md](references/user-guide.md) when the user asks how to operate the skill or needs an onboarding prompt.

Use one mode:

- **journal**: distill the target journal's accepted-paper conventions.
- **author**: distill stable decisions from one author's cross-journal corpus while separating journal, topic, coauthor/lab, time, and editorial effects.
- **hybrid**: build journal and author-associated profiles independently, resolve conflicts, and apply the journal as the formal overlay. Prefer this mode when both corpora are available.

## Create durable project state

For a new long-running project, run:

```bash
python scripts/init_workspace.py <project-directory> --mode hybrid
```

Change the mode as needed. Store decisions and approvals in files rather than relying only on chat history. Never overwrite a non-empty project directory unless the user explicitly authorizes it.

## Workflow

Follow [references/workflow.md](references/workflow.md) for the exact stages, artifacts, and gate semantics.

### Stage 0 — Audit and freeze evidence

Inventory the research question, datasets, versions, inclusion rules, methods, code, figures, tables, statistical outputs, uncertainties, limitations, references, and target-journal constraints.

Check for numerical conflicts, unsupported conclusions, missing provenance, figure/text mismatches, and unresolved analysis choices. Treat “the figures are finished” as insufficient evidence that the scientific content is settled.

Create an evidence register and an unresolved-items list. Stop if a contradiction could materially change the manuscript.

### Stage 1 — Register and screen the corpus

Read [references/corpus-distillation.md](references/corpus-distillation.md).

Create a corpus register. Record why every paper is included, which manuscript sections it can inform, whether the target author plausibly influenced the prose, and what the paper cannot support.

For author mode, include comparison papers from the same journals, periods, topics, and article types when feasible. Do not equate frequency with authorship.

### Mandatory corpus adequacy gate — Prove the corpus is sufficient

Read [references/corpus-adequacy.md](references/corpus-adequacy.md). Use a discovery subset to derive candidate rules and a held-out subset to test them. Assess section coverage, relevance, full-text quality, author-team diversity, attribution metadata, controls, counterexamples, saturation, and cluster-removal stability as applicable.

Create `corpus-adequacy.json` and run:

```bash
python scripts/validate_corpus_adequacy.py path/to/corpus-adequacy.json
```

Apply the verdict strictly:

- **PASS**: continue to the writing contract.
- **SECTION_LIMITED**: stop; continue only for the named eligible sections after the user narrows the scope.
- **FAIL**: stop corpus-derived writing. Request specific missing material, downgrade to a model that passed with explicit user approval, or use a clearly labeled non-corpus-derived workflow.

Hybrid mode passes only when the journal and author-associated models independently pass. Never let one successful model conceal failure of the other.

### Stage 2 — Finalize distilled writing decisions

Read [references/style-contract.md](references/style-contract.md).

Analyze each IMRaD section separately. Distill:

- rhetorical moves and their order;
- paragraph roles and transitions;
- evidence placement and numerical reporting;
- citation placement and comparison logic;
- claim-strength calibration and uncertainty language;
- treatment of exceptions, limitations, and alternative explanations;
- stable traits, conditional traits, and uncertain/confounded traits;
- prohibited phrase-level imitation.

Produce a corpus report and a proposed writing contract. Include counterexamples and uncertainty; do not reduce the corpus to a flattering list of tendencies.

### Mandatory Gate 1 — Approve the writing contract

Present, at minimum:

1. corpus coverage, exclusions, and adequacy verdict;
2. eligible sections and any legitimate mode downgrade;
3. journal profile, author-associated profile, or both;
4. confounds and attribution confidence;
5. section-by-section writing rules;
6. claim-strength rules;
7. prohibited practices and phrase-overlap risks;
8. planned manuscript structure;
9. unresolved scientific issues.

Then stop. Continue only after a new user message explicitly approves or revises the contract. Record the exact approval and timestamp.

### Stage 3 — Build the paragraph blueprint

For every planned paragraph, list:

- paragraph ID and section;
- scientific question and paragraph function;
- topic sentence purpose;
- study evidence and external literature needed;
- allowed inference strength;
- link from the previous paragraph;
- bridge to the next paragraph;
- conclusions the paragraph must not make.

### Mandatory Gate 2 — Approve the blueprint

Show the complete blueprint or one coherent section at a time. Stop until the user explicitly approves it. Approval of the global contract does not automatically approve the blueprint.

### Stage 4 — Draft the bilingual sentence ledger

Read [references/sentence-ledger.md](references/sentence-ledger.md) and [references/integrity-and-citation.md](references/integrity-and-citation.md).

Draft section by section. For every candidate sentence, record:

- stable sentence ID and function;
- English sentence and faithful Chinese translation;
- claim type;
- supporting literature, figure, table, dataset, analysis, method record, or rhetorical role;
- short source excerpt or faithful source note plus an exact locator when literature is used;
- support relation and claim ceiling;
- previous-sentence and next-sentence logic;
- risk flags and approval status.

Do not describe a source as direct support when it is only contextual or analogous. Mark synthesis and inference explicitly.

Validate the machine-readable ledger:

```bash
python scripts/validate_ledger.py path/to/sentence_ledger.jsonl
```

Render a user-readable review document:

```bash
python scripts/render_ledger.py path/to/sentence_ledger.jsonl --output path/to/sentence_ledger.md
```

### Mandatory section gates — Approve sentences

Deliver manageable batches, normally one section at a time. Let the user approve, reject, split, merge, weaken, strengthen, or re-source each sentence. Preserve sentence IDs through revisions.

Never place a sentence marked `drafted`, `needs_revision`, or `rejected` into the clean manuscript.

### Stage 5 — Assemble the clean manuscript

Assemble only `approved` sentences. Remove ledger metadata from the submission manuscript while preserving the ledger as a separate audit artifact.

Enforce this conflict order:

1. evidence and scientific integrity;
2. target-journal hard requirements;
3. explicit user decisions;
4. approved argument structure;
5. stable author-associated decisions;
6. surface preferences.

### Stage 6 — Reverse audit

Audit the assembled manuscript against the evidence register, figures, tables, ledger, writing contract, and journal rules. Verify numbers, citations, modality, causal language, scope, section boundaries, paragraph transitions, abstract/conclusion consistency, and unresolved limitations.

Optionally flag exact phrase overlap as a warning aid:

```bash
python scripts/check_phrase_overlap.py --draft manuscript.txt --corpus-dir corpus-text --n 8
```

Treat the result as a review signal, not a plagiarism verdict. Technical terms and conventional phrases require human interpretation.

## Required deliverables

Maintain these artifacts when the project scope supports them:

- `evidence-register.md`
- `unresolved-items.md`
- `corpus-register.csv`
- `corpus-adequacy.json`
- `corpus-adequacy-report.md`
- `distillation-report.md`
- `writing-contract.md`
- `approval-record.md`
- `paragraph-blueprint.md`
- `sentence-ledger.jsonl`
- `sentence-ledger.md`
- clean manuscript source and rendered manuscript
- `final-audit.md`

## Resource routing

- Read [references/workflow.md](references/workflow.md) for stage outputs, pause behavior, and resumable state.
- Read [references/corpus-distillation.md](references/corpus-distillation.md) before selecting or attributing a journal or author corpus.
- Read [references/corpus-adequacy.md](references/corpus-adequacy.md) before declaring the corpus sufficient or drafting a writing contract.
- Read [references/style-contract.md](references/style-contract.md) before reporting distilled style or drafting the contract.
- Read [references/sentence-ledger.md](references/sentence-ledger.md) before drafting any manuscript sentence.
- Read [references/integrity-and-citation.md](references/integrity-and-citation.md) when mapping claims to evidence, quoting sources, or auditing originality.
- Read [references/user-guide.md](references/user-guide.md) when explaining operation to a user.

Do not load every reference automatically. Load the document needed for the current stage.
