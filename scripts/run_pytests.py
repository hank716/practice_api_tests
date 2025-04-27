
import datetime
import subprocess
import sys
import os
from pathlib import Path

def main():
    output_dir_name = os.getenv("OUTPUT_DIR", "reports")
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / output_dir_name
    reports_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_file = reports_dir / f"pytest_{ts}.html"

    cmd = [
        sys.executable, "-m", "pytest",
        "-q",
        "--html", str(report_file),
        "--self-contained-html",
        "--capture=tee-sys",
        "--log-cli-level=INFO"
    ]

    print(f"[INFO] Running Pytest... Output -> {report_file}")
    sys.exit(subprocess.call(cmd))

if __name__ == "__main__":
    main()
