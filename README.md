# EnergyFlow 360 — Phase 1

Fictional energy-sector Product Owner + JSON Schema training project.

## Setup (macOS)
```bash
cd energyflow360-phase1
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m src.validate_meter
python -m pytest -q
```

Expected: valid sample passes, invalid sample is rejected; tests pass.

## Phase 1 deliverables
- `docs/product_vision.md` — product goal, scope, stakeholders and KPIs
- `docs/discovery_questions.md` — questions to ask stakeholders
- `docs/requirements.md` — initial functional/nonfunctional requirements, assumptions
- `schemas/meter_reading.schema.json` — initial JSON contract (draft for discovery)
- `samples/valid_meter_reading.json` and `samples/invalid_meter_reading.json`
- `src/validate_meter.py` — basic validation proof of concept
- `tests/test_contract.py` — automatic checks

The precise rules are proposed assumptions to be validated with stakeholders in later phases.
