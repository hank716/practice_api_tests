import subprocess
import sys
import os
from pathlib import Path
import shutil

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)

def move_reports_to_ghpages():
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    gh_pages_dir = base_dir / "gh-pages"

    gh_pages_dir.mkdir(exist_ok=True)

    # Copy all reports into gh-pages/
    for report in reports_dir.glob("*.html"):
        shutil.copy(report, gh_pages_dir / report.name)

    print(f"[INFO] Copied reports into {gh_pages_dir}/")

    # Create .nojekyll
    (gh_pages_dir / ".nojekyll").touch()
    print(f"[INFO] Created .nojekyll in {gh_pages_dir}/")

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
