import subprocess
from pathlib import Path
import datetime

def main():
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = reports_dir / f"pytest_{timestamp}.html"

    cmd = [
        "pytest",
        "--html", str(report_path),
        "--self-contained-html",
        "--capture=tee-sys",       # 保留測試中print()
        "--log-cli-level=DEBUG"    # 把log等級放到 DEBUG，列更多細節！
    ]

    subprocess.run(cmd, check=True)

if __name__ == "__main__":
    main()
