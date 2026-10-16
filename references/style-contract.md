# Style analysis and writing-contract schema

## Contents

1. Purpose and observation records
2. Global contract fields
3. Section contracts
4. Claim-strength ladder
5. Paragraph-link contract
6. Approval checklist

## Purpose

Convert corpus observations into executable, falsifiable writing rules. A useful contract says what to do, when to do it, which evidence permits it, and what not to do. Avoid vague labels such as “professional,” “clear,” “Nature-like,” or “high impact.”

## Report observations before rules

For each proposed rule, record:

```text
Rule ID:
Section:
Observed corpus behavior:
Counterexamples:
Likely attribution: journal | author-associated | topic/method | lab/coauthor | time | uncertain
Confidence: stable | conditional | low/confounded
Evidence locations:
Proposed manuscript rule:
When the rule applies:
When the rule must not apply:
Conflict with evidence, user intent, or journal requirements:
```

Do not convert a feature into a rule if the corpus evidence is weak or confounded. Preserve it as an observation instead.

## Global contract fields

Define:

- target journal and article type;
- audience and assumed knowledge;
- central scientific question;
- contribution and claim ceiling;
- terminology and abbreviations;
- coordinate systems, units, and statistical conventions;
- person and voice policy;
- tense policy by section;
- citation style and placement;
- number and uncertainty reporting;
- treatment of null results and exceptions;
- causal-language policy;
- paragraph length as a tendency, not a fixed quota;
- prohibited claims, phrases, and structures;
- expected artifacts and approval gates.

## Section contracts

### Title

Specify:

- whether to lead with phenomenon, method, population, or limitation;
- permitted scope words;
- whether a colon or subtitle is suitable;
- prohibited claims not supported by the full study.

The title must not inherit inflated scope from the corpus.

### Abstract

Define the move sequence, normally a subset of:

1. scientific problem or gap;
2. data/method and scope;
3. principal quantitative findings;
4. boundary or robustness result;
5. implication at the supported scale.

Specify which numbers must appear and which broad claims must not. Do not copy the Introduction's opening sentence.

### Introduction

Define paragraph roles, for example:

1. physical or disciplinary context;
2. established observational or theoretical knowledge;
3. unresolved problem, contradiction, or measurement limitation;
4. why current approaches do not resolve it;
5. precise objectives and manuscript strategy.

Require a genuine gap. Ban unsupported “few studies,” “no study,” or “first” claims unless the search can support them.

### Data and methods

Define the order of:

- instrument/data description;
- sampling and uncertainty;
- event or cohort definition;
- preprocessing and transformations;
- baseline/control design;
- statistical or model procedure;
- validation and sensitivity analysis;
- reproducibility resources.

State what must be cited, what must point to code or data, and what is original to the current study.

### Results

Specify a figure-led order:

1. question or comparison;
2. directly observed pattern;
3. magnitude, uncertainty, and sample support;
4. robustness, exception, or subgroup;
5. minimal handoff to the next result.

Keep mechanisms out unless the journal convention and approved blueprint explicitly permit a brief interpretation. Never hide denominator changes.

### Discussion

Define the recurring paragraph arc, such as:

1. current-study finding;
2. comparison with directly relevant literature;
3. agreement or disagreement with boundary conditions;
4. plausible mechanism;
5. alternative explanation or evidentiary limit;
6. bridge to the next issue.

Specify verbs allowed for direct observations, supported interpretations, and speculative mechanisms. Distinguish physical importance from statistical significance.

### Limitations

Require each limitation to state:

- the affected analysis or claim;
- likely direction or type of impact;
- whether it affects precision, generalizability, or the sign of the conclusion;
- what evidence or design would resolve it.

Avoid apology lists and generic “more work is needed” statements.

### Conclusions

Specify the number and type of findings to retain. Require the conclusion to stay within the body and avoid new citations, mechanisms, numbers, or policy implications unless the target journal permits and the ledger supports them.

### Figures, tables, and captions

Define whether captions are descriptive or interpretive. Require sample sizes, uncertainty meaning, abbreviations, and panel descriptions where needed. Captions must not contain claims absent from the evidence register.

## Claim-strength ladder

Adapt the ladder to the field, but preserve its ordering:

1. **Direct description:** observed, measured, estimated, was higher/lower.
2. **Association:** correlated with, covaried with, was associated with.
3. **Consistency:** is consistent with, supports, agrees with.
4. **Interpretation:** may reflect, likely involves, can be explained by.
5. **Causal conclusion:** caused, drove, determined, demonstrated a mechanism.

Move upward only when design and evidence justify it. A corpus's preferred verb does not raise the user's evidentiary ceiling.

## Paragraph-link contract

For every adjacent paragraph pair, record one link type:

- zoom in or zoom out;
- time, space, altitude, population, or condition change;
- observation to mechanism;
- main effect to robustness;
- agreement to discrepancy;
- result to limitation;
- limitation to future design;
- method to validation;
- question to answer.

A paragraph-ending sentence must not merely repeat the topic sentence. It should close the paragraph's task and create the next task when a transition is needed.

## Contract approval checklist

Before Gate 1, confirm that the contract:

- cites a PASS adequacy verdict, or names the approved sections under SECTION_LIMITED;
- distinguishes evidence rules from style preferences;
- reports corpus counterexamples;
- separates journal and author-associated effects;
- names unresolved scientific choices;
- contains section-specific instructions;
- contains claim ceilings and prohibited moves;
- explains how paragraph logic will be checked;
- cannot be satisfied by copying source prose;
- is short enough for a user to approve deliberately.
