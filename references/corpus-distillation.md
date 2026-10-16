# Journal, author-associated, and hybrid corpus distillation

## Contents

1. Distillation target
2. Corpus modes
3. Corpus selection
4. Author-attribution safeguards
5. Comparison corpus
6. Feature extraction
7. Deconfounding
8. Confidence classification
9. Hybrid conflict resolution
10. Required report

## Distillation target

Distill **writing decisions**, not sentences to reuse. Useful targets include:

- how a section frames its scientific task;
- which rhetorical moves appear and in what order;
- how evidence, numbers, and citations are placed;
- how a paragraph moves from observation to comparison to interpretation;
- how claim strength changes with evidence strength;
- how alternative explanations and limitations are handled;
- how paragraphs hand off to one another.

Treat recurring exact phrases as overlap risks, not desirable style assets.

After registering and provisionally analyzing the corpus, apply the separate hard gate in [corpus-adequacy.md](corpus-adequacy.md). The ranges below guide corpus construction; they do not override the adequacy verdict.

## Corpus modes

### Journal mode

Use accepted papers from the target journal and article type. Prefer papers close in topic, method, data scale, and period. Separate formal rules in the journal guide from empirical tendencies in published papers.

Journal mode estimates the acceptance environment; it does not prove that every observed practice is required or desirable.

### Author mode

Use papers associated with one author across journals, topics, coauthor sets, and time. The output is an **author-associated corpus profile**, not a personal voice model.

Author mode estimates stable research-writing decisions only after likely journal, topic, coauthor/lab, career-stage, and editorial effects are considered.

### Hybrid mode

Build the journal and author-associated profiles independently. Do not blend all papers at ingestion. Compare the two profiles after each has been documented, then resolve conflicts under the hierarchy in `SKILL.md`.

## Corpus selection

Optimize coverage, not raw document count.

Practical starting ranges, not hard statistical thresholds:

- journal profile: roughly 8–15 strongly comparable papers plus the current author guide;
- author-associated exploration: 6–8 author-led papers may reveal hypotheses but has low attribution confidence;
- more reliable author-associated profile: roughly 12–20 papers with variation in journal, year, topic, and coauthors;
- extensive profile: 20–30 papers when the corpus is genuinely heterogeneous and the full text is usable.

Twenty papers from one journal, topic, and coauthor team can be less informative than eight papers spanning several contexts.

### Inclusion criteria

Record whether each paper matches:

- research object and scientific scale;
- measurement or simulation method;
- dependent and explanatory variables;
- study design and article type;
- target journal and publication period;
- target author's likely writing role;
- available full text and extraction quality.

### Exclusion and limitation labels

Use explicit labels:

- duplicate;
- wrong document or mislabeled file;
- unreadable/OCR-limited;
- abstract only;
- corrected or retracted;
- topically adjacent but not direct evidence;
- style-only;
- evidence-only;
- author-role uncertain;
- control paper.

Never report a directory count as the number of papers deeply read.

## Author-attribution safeguards

A multi-author paper does not reveal which author wrote each sentence. Record the target author's role:

- sole author;
- first and corresponding author;
- first author;
- corresponding author;
- co-first or co-corresponding author;
- middle author;
- contribution statement explicitly naming original drafting or review/editing;
- unknown.

Use sole-authored or clearly author-led papers as stronger attribution evidence. Use middle-author papers mainly to test whether a supposed trait persists, not to establish the trait.

Prefer the term “author-associated tendency.” Upgrade confidence only when the tendency persists across contexts and differs from suitable controls.

Do not infer personality, identity, private intent, or personal beliefs from prose.

## Comparison corpus

For every represented journal or major context, sample papers that:

- do not include the target author or core lab when feasible;
- are from a comparable publication period;
- use a similar article type;
- address a nearby topic or method;
- are available in full text.

Ask the counterfactual question:

> If this paper had the same journal, topic, method, and year but not the target author, would the feature probably remain?

If yes, classify it as journal-, topic-, or method-associated rather than author-associated.

## Feature extraction

Analyze every IMRaD section separately. Combine quantitative descriptions with functional reading.

### Rhetorical moves

- context establishment;
- prior finding;
- unresolved gap;
- objective or hypothesis;
- data/method boundary;
- primary observation;
- robustness or exception;
- comparison with literature;
- mechanism proposal;
- alternative explanation;
- limitation;
- implication.

Record move order, optional moves, and counterexamples.

### Paragraph architecture

- primary paragraph function;
- topic-sentence position;
- observation/evidence order;
- comparison and interpretation order;
- position of caveats;
- final-sentence bridge;
- typical number of functional moves per paragraph.

### Sentence and lexical behavior

Use as descriptive support, not as a generation target:

- sentence and paragraph length distributions;
- active/passive decisions by section;
- first-person usage and function;
- hedge and booster use by evidence type;
- causal verbs;
- transition categories;
- citation density and placement;
- numerical reporting density;
- figure/table reference placement.

### Evidence behavior

- whether results precede explanations;
- whether effect size accompanies significance;
- whether uncertainty and sample size are stated;
- how contradictory literature is reconciled;
- whether differences in instrument, scale, or population are made explicit;
- how null or negative results are handled;
- how the author separates consistency from causality.

### Surface phrases

Collect recurring phrases only to:

- identify generic field conventions;
- find likely boilerplate;
- detect signature language that must not be imitated;
- support overlap auditing.

Do not build a phrase bank from distinctive multiword strings.

## Deconfounding

Use this conceptual model:

```text
Observed feature
= author-associated tendency
+ journal convention
+ topic/method requirement
+ coauthor/lab influence
+ time/career-stage change
+ editorial and extraction noise
```

For each proposed trait, complete an attribution matrix:

| Question | Observation | Interpretation | Confidence impact |
|---|---|---|---|
| Appears across journals? |  |  |  |
| Appears across topics/methods? |  |  |  |
| Appears with different coauthor sets? |  |  |  |
| Appears in author-led papers? |  |  |  |
| Absent or weaker in matched controls? |  |  |  |
| Stable over time? |  |  |  |
| Required by journal policy? |  |  |  |
| Could extraction or editing explain it? |  |  |  |

### Time

Partition early, middle, and recent periods when the career span permits it. A systematic recent pattern may be more relevant to a current manuscript than an all-career average. Report evolution rather than calling inconsistency an error.

### Coauthors and labs

Cluster recurring coauthor groups. If a phrase or structure occurs only with one collaborator and appears in that collaborator's other papers, classify it as coauthor/lab-associated or uncertain.

### Topic and method

Do not mistake necessary technical vocabulary or standard reporting order for style. A retrieval paper, an event study, a controlled experiment, and a simulation paper have different evidentiary obligations.

### Journal

Separate hard requirements from soft tendencies. Word limits, structured abstracts, section headings, data statements, and reference format are hard overlays. Published-paper conventions are empirical tendencies and can contain exceptions.

## Confidence classification

### Stable / high confidence

Use when the trait:

- recurs across several contexts;
- appears in author-led papers;
- survives changes in journal, topic, or coauthors;
- is not explained by journal rules or matched controls;
- has clear counterexample analysis.

The trait may influence the writing contract at a structural or epistemic level.

### Conditional / medium confidence

Use when the trait recurs but only under a named condition, such as recent observational papers, Discussion sections, or one article type.

Write a conditional rule, not a universal author claim.

### Confounded or isolated / low confidence

Use when the trait is rare, tied to one journal or collaborator, found mainly in middle-author papers, or indistinguishable from topic and template effects.

Report it as uncertain and exclude it from generation constraints.

## Hybrid conflict resolution

Create a table:

| Decision | Journal profile | Author-associated profile | Evidence/user constraint | Final rule |
|---|---|---|---|---|

Examples:

- If the author uses long abstracts but the journal limits the abstract to 150 words, obey the journal while retaining only the author's high-level move sequence.
- If the author corpus uses strong causal verbs but the user's design is observational, obey the evidence and lower the claim.
- If the journal tends to isolate limitations and the author embeds them locally, use the required limitations section and retain local caveats where needed for honest interpretation.

## Required report

The distillation report must include:

1. corpus question and mode;
2. search/screening boundary;
3. included, excluded, unreadable, duplicate, and control counts;
4. paper-level register;
5. section-specific journal profile;
6. section-specific author-associated profile, if applicable;
7. attribution matrix and confounds;
8. stable, conditional, and excluded traits;
9. time evolution;
10. phrase-level imitation risks;
11. counterexamples;
12. proposed writing rules;
13. unresolved issues;
14. confidence statement.

Present the report before Gate 1 and stop for approval.

Do not present a writing contract unless the enabled corpus model has passed the adequacy gate for the sections governed by that contract.
