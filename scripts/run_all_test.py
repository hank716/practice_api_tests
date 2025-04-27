import subprocess
import sys
from pathlib import Path

def run_script(script_name):
    script_path = Path(__file__).parent / script_name
    if not script_path.exists():
        print(f"[ERROR] {script_name} not found.")
        sys.exit(1)

    print(f"\n[INFO] Running {script_name}...")
    subprocess.run([sys.executable, str(script_path)], check=True)

def main():
    run_script("scripts/run_pytests.py")
    run_script("scripts/run_newman.py")
    print("\n All tests completed successfully!")

if __name__ == "__main__":
    main()
