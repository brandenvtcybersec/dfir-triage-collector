import argparse
from pathlib import Path
from dfir_triage.runner import run, RunConfig


def main():
    parser = argparse.ArgumentParser(description="DFIR Triage Collector")
    parser.add_argument("--case", required=True)
    parser.add_argument("--out", default="cases")
    parser.add_argument("--no-zip", action="store_true")

    args = parser.parse_args()

    config = RunConfig(
        case_id=args.case, out_dir=Path(args.out), zip_output=not args.no_zip
    )

    result = run(config)

    print(f"[+] Case directory created at: {result}")
