# Contributing to Market Scout

First off, thanks for taking the time to contribute! 🎉

Market Scout is a pure Markdown Agent Skill. Contributions can be as simple as
fixing a typo, as useful as adding a new research method, or as big as proposing
a new pipeline stage.

## How Can I Contribute?

### 🐛 Reporting Bugs

Open an issue with:

- **Skill version** (e.g. v3.0.0 — check `SKILL.md` heading)
- **Agent platform** (豆包 / Claude Desktop / Cursor / other)
- **What happened** (the output you got)
- **What you expected**
- **Steps to reproduce** (the prompt you used)

### 💡 Suggesting Enhancements

Open an issue with:

- The problem you're trying to solve
- Why the current workflow doesn't solve it well
- Your proposed approach (if you have one)
- Whether it fits the existing pipeline stages or needs a new one

### 📝 Pull Requests

1. Fork the repo and create a branch from `main`.
2. Make your changes.
3. **Run the self-check** before submitting:
   ```bash
   python tools/validate_skill.py
   ```
   All checks must pass (0 errors).
4. Update `CHANGELOG.md` with your changes under an `Unreleased` section.
5. If you add a new file, update the file structure in `README.md` and the
   manifest in `tools/validate_skill.py`.
6. Submit the PR with a clear title and description.

## Style Guides

### Markdown

- Use ATX-style headings (`#`, `##`, `###`), one H1 per file.
- Leave one blank line between paragraphs and before/after code blocks.
- Use fenced code blocks with language tags (```yaml, ```json, ```text, ```python).
- Tables: max 6 columns for mobile readability; use key-value lists for narrow content.
- Chinese as the primary language for method docs; key terms in English in parentheses.
- Status codes and field names in English (`GO`, `Demand Strength`, `MS-101`).

### Methodology Content

- Every scoring dimension must be evidence-bound (score + reason + evidence + uncertainty).
- No "the market is huge" style conclusions without evidence.
- Preserve the three independent code systems: evidence grade (A/B/C), delivery state
  (HYPOTHESIS→…→PRODUCTIZED), and pipeline stage (FIND/VALIDATE/…). Do not reuse codes.
- New pipeline stages must define input/output data contracts and failure/fallback rules.

### Python (tools/)

- Python 3.8+, no third-party dependencies.
- Add docstrings and type hints.
- Exit code 0 = pass, 1 = fail.
- Print a human-readable summary at the end.

## Project Structure

See `README.md` → 📁 Project Structure for the full layout. Key directories:

- `references/` — methodology documents (one file per method/module)
- `templates/` — fill-in templates for each stage card and the final report
- `examples/` — end-to-end workflow examples (all data is illustrative)
- `tools/` — self-check and utility scripts

## Versioning

We use [Semantic Versioning](https://semver.org/):

- **MAJOR** (x.0.0): breaking changes to the pipeline, data contracts, or core methodology
- **MINOR** (0.x.0): new pipeline stage, new methodology, new template (backward-compatible)
- **PATCH** (0.0.x): bug fixes, typo fixes, documentation improvements

## Questions?

Open an issue and tag it `question`. We'll get back to you.

---

Thanks again for contributing — every improvement helps someone get closer to
their first real payment. 💪
