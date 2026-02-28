import platform
from pathlib import Path
from typing import Dict, Any

from dfir_triage.utils.shell import run_cmd


def is_windows() -> bool:
    return platform.system().lower() == "windows"


def collect_windows(case_dir: Path) -> Dict[str, Any]:
    raw_dir = case_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)

    commands = [
        ("hostname", "hostname"),
        ("systeminfo", "systeminfo"),
        ("tasklist", "tasklist"),
        ("netstat", "netstat -ano"),
        ("ipconfig", "ipconfig /all"),
    ]

    results = []

    for name, cmd in commands:
        res = run_cmd(cmd, timeout=300)
        out_path = raw_dir / f"{name}.txt"
        out_path.write_text(res.stdout + res.stderr, encoding="utf-8", errors="replace")

        results.append(
            {
                "name": name,
                "cmd": cmd,
                "returncode": res.returncode,
                "output_file": str(out_path.relative_to(case_dir)),
            }
        )

    return {"collector": "windows", "results": results}
