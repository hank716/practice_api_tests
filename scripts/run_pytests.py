import subprocess
from pathlib import Path
import datetime

def main():
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = reports_dir / f"pytest_{timestamp}.html"

    cmd = [
        "pytest", "tests/",
        "--html", str(report_path),
        "--self-contained-html",
        "--capture=tee-sys",       # ✅ pytest執行中print出來的東西也一起輸出
        "--log-cli-level=DEBUG"    # ✅ pytest執行中log (logging.debug/info/warning...) 也即時輸出
    ]

    print(f"[INFO] Running Pytest... Output -> {report_path}")
    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
