# Contributing

Use original prose and cite sources actually inspected. Keep the suite general across disciplines and the installed folders self-contained.

## Propose a change

Open an issue or pull request describing the task, affected module, smallest synthetic input, observed output and expected behavior. Show why the proposed wording changes an agent's decision. Do not add blanket rules for a single field or promise stronger results than the evidence supports.

For behavior changes, record a baseline without the proposed instruction and a fresh-context test with it. Report baseline successes and failures honestly. Preserve the common integrity contract across modules; if it changes, rerun the shared cases. Do not grade a quoted bad example as an actual violation.

## Maintainer checks

Python 3.10 or later is needed only for repository development checks:

```sh
python -m unittest discover -s tests -p test_validation.py
python scripts/validate.py
```

The validator checks this repository's simple metadata, links, contract consistency and packaging. It is not a general YAML parser, a detector or a scientific validity check. Full frontmatter checks should also use an Agent Skills validator.

Read [evaluation](docs/evaluation.md), [sources](docs/sources.md) and [security](SECURITY.md). Keep private research files, full papers and temporary results out of Git. No extra packages are needed to use the installed instructions.

## Text encoding

Installable `SKILL.md` and `agents/openai.yaml` files must use UTF-8 **without a BOM**. `SKILL.md` must begin directly with `---`; bytes before that delimiter can prevent Codex from recognizing its frontmatter. The repository validator rejects a leading BOM in either installed file type. Do not normalize or strip a BOM before validating these files: that hides the defect. Other documents may use UTF-8 with a BOM when their consumers support it.
