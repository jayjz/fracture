# Contributing to Fracture

This is currently a solo research project with a tightly scoped roadmap.

PRs are welcome once the core matrix (Phase 1–5) is complete and the evaluation set is locked. Until then, the highest-value contributions are:

1. Well-reasoned issues about failure taxonomy or evaluation design
2. Reproducible bug reports on the injectors or metrics
3. Additional carefully designed tasks that stress the existing failure modes

## Development Setup

```bash
git clone https://github.com/jayjz/fracture.git
cd fracture
python -m venv .venv
source .venv/bin/activate   # or Windows equivalent
pip install -e ".[dev]"
```

## Code Style

- Ruff for linting and formatting
- Type hints required on public interfaces
- Prefer small, focused modules
- Docstrings on all public classes and functions

## Principles for Contributors

- Do not expand scope beyond the current roadmap without discussion
- Prefer improving evaluation quality over adding new topologies
- Keep injectors independent of topologies
- Any change that affects experimental results must be versioned or clearly documented
