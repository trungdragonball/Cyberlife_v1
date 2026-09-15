# CyberLife V1 — Locked Codebase

This repository is generated from the locked CyberLife V1 architecture, logic contracts,
module registry, and simulation/test invariants.

Architecture: one application, modular monolith, domain-driven, interface-first.
This is the engineering starting codebase: modules are represented with explicit
contracts, boundaries, safety rules, and tests so an engineer can run and extend it.

It is intentionally NOT a microservice split and NOT a V1.5 codebase.

Run:
  python -m venv .venv
  source .venv/bin/activate   # Windows: .venv\Scripts\activate
  pip install -r requirements.txt
  pytest -q
  uvicorn apps.cyberlife.main:app --reload

Docker:
  docker compose up --build

See docs/LOCKED_CONTRACT.md and docs/MODULE_REGISTRY.md.
