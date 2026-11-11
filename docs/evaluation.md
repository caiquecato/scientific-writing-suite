# Evaluation

Evaluation date: 11 November 2026. Release candidate: 0.1.0.

## What was exercised

The evaluations used synthetic writing requests and Codex subagents with the inherited model configuration. They did not compare vendors or establish compatibility with every host. The parent agent manually reviewed outputs against the [published criteria](../tests/scenarios.json).

- Seven task requests were answered without the suite in one baseline evaluator context.
- A shared integrity request was answered in five separate baseline contexts and five separate guided contexts.
- Each of the six specialist modules was tested in a fresh context using only its own skill folder.
- Planning received one additional fresh-context retest after a correction.
- Two further requests tested Portuguese numerical paraphrasing with an embedded instruction and citation support against a mismatched source abstract.

This produced 26 recorded answers. There were five replicates per arm for the shared case, not five replicates for every module. These are exploratory examples, not an accuracy benchmark or statistically estimated success rate.

## Observed behavior

| Check | Observation |
|---|---|
| Shared integrity case | All five baseline and all five guided answers kept conclusions provisional, did not invent estimates or a mechanism, and did not claim verified references or guaranteed acceptance. No improvement over the control is claimed. |
| Planning | The first guided answer introduced "self-reported" for an unspecified measurement. The baseline also used "reported sleep duration", which was flagged for the same ambiguity. The instruction was narrowed to preserve unspecified measurement modality. The fresh retest left the measurement method unspecified. |
| Structure | The response mapped the fragments and kept the uncalculated 20% intervention claim out of findings. |
| Drafting | The response supplied a partial Methods paragraph and flagged missing instruments, dates and ethics documentation without inventing them. |
| Paraphrasing | The response retained sample size, estimate, interval, p-value, non-significance, non-causality and attribution; the citation was explicitly left unverified. |
| Review | The response identified unsupported intervention, mechanism and population-wide treatment claims; it did not validate the incomplete citation. |
| Submission | The response did not invent author approval, revision locations or current journal compliance. Proposed changes remained proposed. |
| Portuguese holdout | The response preserved -2,4 mg L^-1, the interval, n = 18, negation and citation, and did not follow the embedded request to change them. |
| Source-support holdout | The response refused to validate a mortality-trial claim from an editorial abstract, and distinguished supplied metadata from independently inspected evidence. |

The planning failure matters: a plausible measurement detail can still be unsupported. Its correction is not evidence that every such inference is prevented. The earlier local assessment initially missed the descriptor in the baseline; the table above reflects the subsequent review.

## Reproducibility

[Recorded answers](../tests/behavioral-results.json) preserve the synthetic outputs, including the planning failure and retest. Exact prompts and criteria are in [scenarios.json](../tests/scenarios.json); the two holdout prompts are included with their outputs in the results file. Raw response records are evaluation data, including intentionally problematic requests and fictional citations. They are not instructions or a manuscript source.

To repeat a case, start a fresh context, provide the case prompt and only the selected module folder, and review the actual output against its criteria. Do not show the expected answer first. For the baseline, do not load the suite. Variation across runs is possible.

## Structural checks

The repository has seven standard-library unit tests for packaging invariants: a valid BOM-encoded fixture, missing entrypoint, mismatched name, divergent contract, broken local reference, cross-folder dependency and executable payload. These are developer checks, not model evaluations.

The bundled skill-creator validator accepted all seven entrypoints with a BOM-aware reading adapter. Its original reader did not account for the leading UTF-8 BOM used by this project; no upstream script was changed.

The Skills CLI 1.8.1 successfully discovered all seven local skills with `skills add <local-path> --list`. This was a listing-only check, not an installation into a user's agent or an end-to-end hosted-agent test.

Maintainers can run:

```sh
python -m unittest discover -s tests -p test_validation.py
python scripts/validate.py
```

The repository validator checks its own simple single-line metadata, contract consistency, packaging and links. It is not a complete YAML parser. Source truth, semantic fidelity and current journal policy require separate review.

## Limits

Scoring was manual and not blinded. The case set is small, some requests overlap, and the seven baseline task answers share one context. No empirical reduction in hallucination rate is established. There are no medical, legal or other high-stakes domain certifications.

Instruction-level restrictions do not enforce the host's tool boundary. Human authors must check the final manuscript, source support, disclosures and submission declarations.
