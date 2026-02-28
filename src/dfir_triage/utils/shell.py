import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class CmdResult:
    cmd: str
    returncode: int
    stdout: str
    stderr: str
    started_utc: str
    ended_utc: str

def run_cmd(cmd: str, timeout: int = 120) -> CmdResult:
    started = datetime.now(timezone.utc)
    p = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
        timeout=timeout,
        encoding="utf-8",
        errors="replace",
    )
    ended = datetime.now(timezone.utc)

    return CmdResult(
        cmd=cmd,
        returncode=p.returncode,
        stdout=p.stdout or "",
        stderr=p.stderr or "",
        started_utc=started.isoformat(),
        ended_utc=ended.isoformat(),
    )