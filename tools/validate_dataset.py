import argparse, json, sys
from pathlib import Path
import yaml
import pandas as pd
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]

def load_schema(name):
    with open(ROOT / "schemas" / name, "r") as f:
        return json.load(f)

MORPH = load_schema("morphology.schema.json")
CONTEXT = load_schema("context.schema.json")

def validate_yaml(path, schema):
    with open(path, "r") as f:
        data = yaml.safe_load(f)
    Draft202012Validator(schema).validate(data)

def validate_csv_header(path, required):
    df = pd.read_csv(path, nrows=1)
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise ValueError(f"{path}: missing columns {missing}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=str, default=str(ROOT / "data"))
    args = ap.parse_args()
    root = Path(args.root)

    for y in root.glob("morphologies/*.yaml"):
        validate_yaml(y, MORPH)
        print(f"[OK] morphology {y.name}")
    for y in root.glob("contexts/*.yaml"):
        validate_yaml(y, CONTEXT)
        print(f"[OK] context {y.name}")

    required = "t,q_j1,qd_j1,tau_j1,I_j1,V_j1,P_j1".split(",")
    for c in root.glob("episodes/*.csv"):
        validate_csv_header(c, required)
        print(f"[OK] episode {c.name}")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"[FAIL] {e}")
        sys.exit(1)
