import subprocess
import sys
import shutil
import time
from pathlib import Path

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"[ERROR] {script_name} not found.")
        sys.exit(1)

    print(f"\n[INFO] Running {script_name}...")
    subprocess.run([sys.executable, str(script_path)], check=True)

def wait_for_reports(reports_dir, timeout=10):
    """等待 reports/ 有產生html，最多等timeout秒"""
    for _ in range(timeout):
        if any(reports_dir.glob("*.html")):
            return
        time.sleep(1)
    print("[WARN] No HTML reports generated after waiting.")

def copy_reports_to_gh_pages():
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / "reports"
    gh_pages_dir = base_dir / "gh-pages"
    gh_pages_dir.mkdir(parents=True, exist_ok=True)

    wait_for_reports(reports_dir)

    for html_file in reports_dir.glob("*.html"):
        shutil.copy(html_file, gh_pages_dir)
        print(f"[INFO] Copied {html_file.name} to gh-pages/")

def main():
    run_script("run_pytests.py")
    run_script("run_newman.py")
    copy_reports_to_gh_pages()
    run_script("generate_index.py")

    print("\n All tests completed and reports prepared!")

if __name__ == "__main__":
    main()
