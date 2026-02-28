import json
from datetime import datetime, timezone
from pathlib import Path

from dfir_triage.collectors.windows import is_windows, collect_windows
from dfir_triage.utils.hashing import sha256_file
from dfir_triage.utils.packaging import zip_dir


def _utc_now():
    return datetime.now(timezone.utc).isoformat()


class RunConfig:
    def __init__(self, case_id: str, out_dir: Path, zip_output: bool = True):
        self.case_id = case_id
        self.out_dir = out_dir
        self.zip_output = zip_output


def run(config: RunConfig):
    case_dir = config.out_dir / config.case_id
    case_dir.mkdir(parents=True, exist_ok=True)

    if not is_windows():
        raise RuntimeError("Only Windows supported for now")

    summary = collect_windows(case_dir)

    manifest = {
        "case_id": config.case_id,
        "started_utc": _utc_now(),
        "collector": summary["collector"],
        "files": [],
    }

    for p in case_dir.rglob("*"):
        if p.is_file():
            manifest["files"].append(
                {"path": str(p.relative_to(case_dir)), "sha256": sha256_file(p)}
            )

    (case_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )

    if config.zip_output:
        zip_path = config.out_dir / f"{config.case_id}.zip"
        zip_dir(case_dir, zip_path)

    return case_dir
