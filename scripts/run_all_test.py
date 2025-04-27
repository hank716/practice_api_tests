import subprocess
import sys
import os
from pathlib import Path
import shutil
import datetime

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)

def move_reports_to_ghpages():
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    gh_pages_dir = base_dir / "gh-pages"

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    version_dir = gh_pages_dir / timestamp
    version_dir.mkdir(parents=True, exist_ok=True)

    # Copy all reports into timestamped folder
    for report_file in reports_dir.glob("*.html"):
        shutil.copy(report_file, version_dir / report_file.name)

    print(f"[INFO] Copied reports into {version_dir}/")

    # Create .nojekyll if not exist
    (gh_pages_dir / ".nojekyll").touch(exist_ok=True)
    print(f"[INFO] Ensured .nojekyll exists in {gh_pages_dir}/")

def main():
    print("[INFO] Running Pytest...")
    run_script("run_pytests.py")

    print("[INFO] Running Newman...")
    run_script("run_newman.py")

    move_reports_to_ghpages()

    print("[INFO] Generating Index HTML...")
    run_script("generate_index.py")

if __name__ == "__main__":
    main()
