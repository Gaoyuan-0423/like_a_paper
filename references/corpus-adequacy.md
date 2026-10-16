# Corpus adequacy gate

## Contents

1. Purpose and verdicts
2. General requirements
3. Journal-model requirements
4. Author-associated-model requirements
5. Section and relevance coverage
6. Discovery/validation protocol
7. Cluster-removal test
8. Hybrid-mode rule
9. Adequacy record and gate behavior

## Purpose

Prevent the agent from declaring a journal or author-associated writing model ready merely because some papers were uploaded. Corpus size is necessary but not sufficient. Require coverage, relevance, attribution, variation, extraction quality, counterexample search, and out-of-sample stability before corpus-derived rules can govern manuscript writing.

Passing this gate means the corpus is adequate for the stated scope. It does not guarantee publication, scientific correctness, or authorship attribution.

## Verdicts

Use exactly three verdicts:

- **PASS**: the enabled model meets every hard requirement for every requested manuscript section.
- **SECTION_LIMITED**: global requirements pass, but only named sections have adequate examples. Corpus-derived writing is allowed only for those sections after user approval.
- **FAIL**: one or more global hard requirements fail. Do not use the failed model to generate corpus-derived manuscript prose.

There is no “user accepts the risk, therefore call it PASS” option. The user may instead:

1. provide more or better papers;
2. narrow the requested sections;
3. switch from hybrid to the model that passed;
4. proceed with generic evidence-grounded writing while explicitly abandoning the claim of corpus-derived style.

## General requirements for every enabled model

Require all of the following:

- full text, not abstract-only access, for counted papers;
- readable target sections and reliable extraction;
- a documented inclusion/exclusion register;
- a discovery/validation split fixed before final rules are declared;
- a documented search for counterexamples;
- no major proposed rule invalidated by the held-out papers;
- no new high-confidence rule introduced by the final validation batch;
- exact phrases excluded from model traits;
- no critical extraction gap in a requested section;
- section coverage evaluated separately.

The validation set must not be used to invent the initial rules and then described as independent confirmation. If validation changes a major rule, revise the rule and obtain another untouched validation batch or collect additional papers.

## Journal-model hard requirements

Use these conservative default floors:

1. At least **8** usable full-text papers from the target journal and relevant article type.
2. At least **5** papers directly comparable in topic, method, data scale, or scientific task.
3. A verified current journal author guide or equivalent formal requirements source.
4. At least **3** independent author teams, to avoid treating one laboratory's habits as journal style.
5. At least **2** publication periods or year bands, to reduce special-issue and short-term editorial effects.
6. At least **2** held-out validation papers.
7. At least **4** usable examples for each manuscript section that will be governed by the journal model.
8. Held-out papers confirm the proposed high-confidence rules.
9. No major high-confidence rule is invalidated.
10. The latest validation batch adds no new high-confidence rule.
11. Counterexample search is documented even when no counterexample is found.
12. No critical extraction gap affects a requested section.

Do not count editorials, perspectives, reviews, letters, and full research articles as interchangeable. Match the intended article type.

## Author-associated-model hard requirements

Use these conservative default floors:

1. At least **10** usable full-text papers associated with the target author.
2. At least **6** author-led papers: sole author, first author, corresponding author, co-first/co-corresponding author, or explicit original-draft contribution.
3. At least **2** journals.
4. At least **2** coauthor or laboratory configurations.
5. At least **2** time bands, topic/method contexts, or other independent contexts beyond journal; record why the selected variation can reveal stable traits.
6. At least **4** matched control papers spanning at least **2** relevant contexts.
7. Authorship-role or contribution metadata for at least **60%** of counted papers.
8. At least **2** held-out validation papers.
9. At least **4** usable examples for each manuscript section governed by the author-associated model.
10. Held-out papers confirm the proposed high-confidence rules.
11. Stable rules persist after removing the largest journal, coauthor, or lab cluster.
12. No major high-confidence rule is invalidated.
13. The latest validation batch adds no new high-confidence rule.
14. Counterexample search is documented.
15. Phrase-level traits are excluded from generation rules.
16. No critical extraction gap affects a requested section.

If the target author has too few publications to meet these floors, call the analysis exploratory. Do not relabel an exploratory profile as a stable author-associated model.

## Why the floors differ

Journal papers are direct observations of an editorial environment, although individual author teams still create variation. Author-associated papers are noisier because prose authorship is uncertain and must be separated from journal, team, topic, and career-stage effects. The author model therefore requires role evidence, controls, and leave-largest-cluster-out stability.

## Section-level adequacy

Evaluate every requested section independently:

- title/abstract;
- introduction;
- data and methods;
- results;
- discussion;
- limitations;
- conclusions;
- captions or supplements when requested.

If a corpus contains eight usable Discussions but only two complete Methods sections, it may pass for Discussion and fail for Methods. Do not let overall paper count hide a section deficit.

For sections that do not exist as separate headings in the corpus, map the functional content explicitly. For example, a limitation may be embedded in Discussion. Count it only if its rhetorical role can be reliably identified.

## Relevance requirement

Classify papers as:

- **direct**: close scientific task, method/data type, scale, and article type;
- **adjacent**: useful for a subset of decisions but not directly comparable;
- **style-only**: useful for journal conventions but not scientific evidence;
- **evidence-only**: supports a claim but should not determine the target style;
- **control**: used to separate author effects from journal/topic/team effects.

Only direct papers count toward the journal model's directly relevant floor. A large style-only corpus cannot compensate for missing direct papers.

## Discovery and validation protocol

1. Stratify papers by journal, year, topic/method, author team, and author role.
2. Reserve at least two eligible papers as a validation set before finalizing rules.
3. Derive candidate rules from the discovery set.
4. Test each high-confidence rule against validation papers.
5. Record confirmation, boundary condition, counterexample, or invalidation.
6. Add a new batch if validation changes a major rule.
7. Declare saturation only when the final batch adds no new high-confidence rule and does not materially alter an existing one.

Do not use “the same phrases appeared again” as stability evidence. Validate rhetorical functions and decisions.

## Leave-largest-cluster-out test for author mode

Identify the largest potential confound cluster, such as:

- one journal;
- one recurring coauthor team;
- one laboratory;
- one topic/method family;
- one career period.

Remove that cluster and re-evaluate every proposed stable author-associated rule. A rule that disappears is cluster-dependent and must be downgraded to conditional or confounded.

## Hybrid-mode rule

Hybrid mode passes only if both the journal model and author-associated model independently pass for the requested sections.

If only one model passes:

- return **FAIL for hybrid**;
- identify the passing model;
- recommend a named downgrade, such as `journal` mode;
- require explicit user approval of the downgraded contract;
- do not silently borrow traits from the failed model.

If both models pass overall but differ by section, hybrid writing is allowed only in the intersection of their eligible sections. Other sections require a different approved mode.

## Corpus adequacy record

Create `corpus-adequacy.json` and validate it with:

```bash
python scripts/validate_corpus_adequacy.py path/to/corpus-adequacy.json
```

Also create a human-readable `corpus-adequacy-report.md` containing:

- enabled mode;
- requested sections;
- counts and eligibility definitions;
- failed and passed requirements;
- section-level coverage;
- discovery/validation split;
- counterexamples and invalidated rules;
- saturation evidence;
- author-attribution limitations;
- final verdict;
- permitted next action.

## Gate behavior

- On **PASS**, proceed to drafting the writing contract, then stop at Gate 1 for user approval.
- On **SECTION_LIMITED**, present the eligible sections and stop. Continue only if the user narrows the authorized scope accordingly.
- On **FAIL**, stop corpus-derived writing. Request specific missing materials or offer an explicitly different, non-corpus-derived workflow.

Never describe a FAIL or SECTION_LIMITED corpus as fully distilled.
