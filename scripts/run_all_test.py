import subprocess, sys, pathlib

def run_script(script):
    res = subprocess.run([sys.executable, str(pathlib.Path(__file__).parent / script)])
    return res.returncode

def main():
    codes = []
    for script in ("run_pytests.py", "run_newman.py"):
        codes.append(run_script(script))

    # 一定要生 index.html
    run_script("generate_index.py")

    worst = max(codes)          # 0=全部成功，>0 代表至少一支失敗
    if worst != 0:
        print(f"[WARN] one or more test stages failed, exit={worst}")
    sys.exit(worst)

if __name__ == "__main__":
    main()
