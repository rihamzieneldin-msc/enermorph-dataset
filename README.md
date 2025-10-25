# EnerMorph Dataset (Real Hardware)

**Context-rich, morphology–energy dataset** for training and evaluating energy-aware policy transfer across heterogeneous robots.  
Runs are collected **on real platforms**, not simulation, with standardized morphology (json), context (json), and episode logs (CSV).

## Structure
```
data/
 ├─ morphologies/  # per-robot json (static hardware & wiring)
 ├─ contexts/      # per-scenario json (task & environment)
 ├─ episodes/      # per-run CSV (time-series logs)
 └─ metadata/      # feature maps, units, docs
```

## Quick start
```bash
git lfs install
git clone https://github.com/<you>/enermorph-dataset.git
cd enermorph-dataset
python -m venv .venv && source .venv/bin/activate
pip install -r tools/requirements.txt
python tools/validate_dataset.py --root data
```

## Templates
- `templates/morphology_template.yaml` – fill once per robot.
- `templates/context_template.yaml` – fill once per scenario.
- `templates/episode_header.csv` – copy header when logging runs.

## Validation (CI)
Every PR runs:
- JSON Schema checks for YAML,
- CSV header compliance,
- basic unit checks (SI units flagging).

## Citation
If you use this dataset or spec, please cite (see `CITATION.cff`).
