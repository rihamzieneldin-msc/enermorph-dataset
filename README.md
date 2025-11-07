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


## Validation (CI)
Every PR runs:
- JSON Schema,
- CSV header compliance,
- basic unit checks (SI units ).

