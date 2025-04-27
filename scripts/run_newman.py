import datetime, subprocess, sys, re
from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn, TimeRemainingColumn

def main():
    reports_dir = Path(__file__).parent.parent / "reports"
    reports_dir.mkdir(exist_ok=True)

    ts = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_file = reports_dir / f"postman_{ts}.html"

    cmd = [
        "newman", "run", "collection/PracticeSoftwareTesting_API_Collection.json",
        "-r", "cli,htmlextra",
        "--reporter-htmlextra-export", str(report_file),
        "--color", "on"
    ]

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1
    )

    total_reqs = None
    task_id = None

    # rich progress bar
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
            print(line, end="")  # keep orignal newman's CLI output

            if total_reqs is None:
                m = re.search(r"Total requests:\s+(\d+)", line)
                if m:
                    total_reqs = int(m.group(1))
                    task_id = progress.add_task("Running API tests", total=total_reqs)

            if task_id is not None and line.startswith("→"):
                progress.update(task_id, advance=1)

        ret = proc.wait()

    if ret != 0:
        sys.exit(ret)

if __name__ == "__main__":
    main()
