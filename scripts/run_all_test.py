import subprocess
import sys
import shutil
import datetime
from pathlib import Path

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)

def clean_reports_folder():
    reports_dir = Path(__file__).parent.parent / "reports"
    if reports_dir.exists():
        for file in reports_dir.glob("*.html"):
            file.unlink()
        print(f"[INFO] Cleaned old reports in {reports_dir}")

def move_reports_to_ghpages():
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    gh_pages_dir = base_dir / "gh-pages"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    version_dir = gh_pages_dir / timestamp
    version_dir.mkdir(parents=True, exist_ok=True)

    for report in reports_dir.glob("*.html"):
        shutil.copy(report, version_dir / report.name)

    print(f"[INFO] Copied latest reports into {version_dir}")

    (gh_pages_dir / ".nojekyll").touch(exist_ok=True)
    print(f"[INFO] Ensured .nojekyll exists")

def main():
    clean_reports_folder()
    run_script("run_pytests.py")
    run_script("run_newman.py")
    move_reports_to_ghpages()
    run_script("generate_index.py")

if __name__ == "__main__":
    main()
