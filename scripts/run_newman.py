import datetime
import subprocess
import sys
import os
import re
from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

def main():
    output_dir_name = os.getenv("OUTPUT_DIR", "reports")
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / output_dir_name
    reports_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_file = reports_dir / f"postman_{ts}.html"

    cmd = [
        "newman", "run", "collection/PracticeSoftwareTesting_API_Collection.json",
        "-r", "cli,htmlextra",
        "--reporter-htmlextra-export", str(report_file),
        "--color", "on"
    ]

    print(f"[INFO] Running Newman... Output -> {report_file}")

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    total_reqs = None
    task_id = None

    progress = Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]{task.description}"),
        BarColumn(bar_width=None),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeElapsedColumn(),
        TimeRemainingColumn()
    )

    with progress:
        for line in proc.stdout:
            print(line, end="")

            if total_reqs is None:
                m = re.search(r"Total requests:\s+(\d+)", line)
                if m:
                    total_reqs = int(m.group(1))
                    task_id = progress.add_task("Running API requests", total=total_reqs)

            if task_id is not None and line.startswith("→"):
                progress.update(task_id, advance=1)

        ret = proc.wait()

    if ret != 0:
        sys.exit(ret)

if __name__ == "__main__":
    main()