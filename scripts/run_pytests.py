import datetime, subprocess, sys
from pathlib import Path

def main():
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_file = reports_dir / f"pytest_{ts}.html"

    cmd = [
        sys.executable, "-m", "pytest",
        "-q",
        "--html", str(report_file),
        "--self-contained-html",
        "--capture=tee-sys",            # ✱ output to terminal+html
        "--log-cli-level=INFO"          # ✱ open live log
    ]

    print("[INFO] Running tests …")
    sys.exit(subprocess.call(cmd))

if __name__ == "__main__":
    main()
