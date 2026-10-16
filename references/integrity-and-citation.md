# Evidence, citation, and originality rules

## Contents

1. Evidence and sentence classification
2. Citation verification
3. Current-study evidence
4. Inference, translation, and source excerpts
5. Originality and phrase-overlap screening
6. Journal/author corpus boundaries
7. Final audit

## Evidence is not stylistic resemblance

A source supports a manuscript sentence because its data, method, or argument bears on the proposition—not because it contains similar words. Reject phrase-based source matching.

Classify each sentence before selecting evidence:

- external field claim;
- current-study result;
- method or definition;
- author inference or synthesis;
- limitation;
- objective;
- rhetorical transition.

Use the corresponding evidence type in the sentence ledger.

## Citation verification

For each literature citation:

1. read the relevant source passage in context;
2. record a page, section, paragraph, figure, table, or stable local locator;
3. verify population, instrument, spatial/temporal scale, method, and outcome;
4. identify whether support is direct, partial, analogous, contextual, methodological, or contrasting;
5. preserve the source's uncertainty and boundary conditions;
6. verify bibliographic identity and corrections when the citation is consequential;
7. avoid citing a review as if it were the primary observation when the primary source is available and needed.

Do not let one citation appear to support several unrelated clauses. Split the sentence or map evidence clause by clause.

## Current-study evidence

Statements about the user's results normally cite project artifacts rather than external papers:

- figure and panel;
- table and row/column;
- analysis output and exact metric;
- dataset version and subset;
- code/configuration and parameter;
- approved method record.

An external paper may contextualize or compare the result but does not validate the user's number by resemblance.

## Inference and mechanism

For an interpretive sentence, identify:

- the current observation being interpreted;
- the external or theoretical basis;
- plausible alternatives;
- what the design cannot distinguish;
- the maximum allowed verb.

Prefer constructions such as “is consistent with,” “may reflect,” or “supports the interpretation” when the mechanism is not directly identified. Do not automatically weaken every sentence; direct measurements should remain direct.

## Translation integrity

Check English and Chinese in both directions. Common errors include:

- translating `may` as an unqualified assertion;
- translating association as influence or causation;
- dropping population or time qualifiers;
- changing “one possible explanation” into “the reason”;
- omitting negative, null, or exception language;
- changing the denominator or statistical unit;
- replacing “not statistically distinguishable” with “the same.”

Flag any strength mismatch before user review.

## Source excerpts

Use excerpts only to let the user verify the mapping. Keep them short and attach a locator. Prefer a concise paraphrase when a longer passage would be required.

Do not reproduce large portions of a paper, a sequence of adjacent sentences, or a collection of excerpts that substitutes for the source. Do not expose licensed full text in final public artifacts.

An excerpt is not permission to reuse its wording in the manuscript.

## Originality and patchwriting

Patchwriting includes:

- swapping synonyms while preserving source syntax;
- stitching clauses from several papers;
- preserving a source paragraph's sentence sequence with cosmetic changes;
- translating a source sentence and translating it back into English;
- using a distinctive phrase bank from one author;
- treating citation as permission to copy prose.

Draft from the evidence proposition and approved rhetorical function, not from the source sentence. After drafting, compare against the source and revise suspicious overlap without changing scientific meaning.

## Phrase-overlap screening

The overlap script flags exact contiguous word sequences. It cannot determine plagiarism, authorship, fair use, or whether a phrase is conventional.

Review each match for:

- technical terminology that cannot be paraphrased;
- required instrument or method names;
- generic academic phrases;
- quoted and attributed material;
- distinctive source wording;
- repeated syntax beyond the matching words.

Treat an eight-word match as a review trigger, not an automatic violation. Shorter thresholds create many false positives; longer thresholds miss close paraphrases.

## Journal and author-corpus integrity

The target journal may legitimately determine:

- section order;
- abstract structure and length;
- formatting and reporting requirements;
- data/code statements;
- citation format.

An author-associated corpus may inform:

- argument order;
- evidence placement;
- claim calibration;
- handling of comparisons and limitations;
- paragraph transitions.

It must not supply recognizable personal voice, signature phrasing, or a false claim that the target author would endorse the manuscript.

## Citation density

Do not optimize for citations per sentence. Optimize for:

- complete support of external claims;
- primary and directly relevant evidence;
- appropriate comparison across methods and scales;
- clear separation of literature evidence and current-study evidence;
- avoidance of ornamental citation clusters.

Transitions, objectives, and direct descriptions of the user's own results may legitimately have no external citation.

## Final audit questions

- Can every number be traced to an artifact?
- Does every external factual claim have verified support?
- Does each citation support the exact nearby proposition?
- Are comparison conditions explicit?
- Are observation and interpretation separated?
- Are alternative explanations represented fairly?
- Does every causal verb meet the design's claim ceiling?
- Does the Chinese translation preserve modality?
- Does any phrase resemble a source more than necessary?
- Did assembly introduce unapproved wording?
- Do the abstract, title, and conclusion remain within the body evidence?
