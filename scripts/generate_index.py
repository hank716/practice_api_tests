import datetime
import os
from pathlib import Path

def main():
    output_dir_name = os.getenv("OUTPUT_DIR", "reports")
    base_dir = Path(__file__).parent.parent
    reports_dir = base_dir / output_dir_name
    reports_dir.mkdir(parents=True, exist_ok=True)

    index_html = base_dir / "index.html"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report_files = sorted(
        [p for p in reports_dir.glob("*.html")],
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )

    rows = ""
    for f in report_files:
        rows += f"""<tr><td>{f.name}</td><td><a href="{output_dir_name}/{f.name}" target="_blank">View</a></td></tr>\n"""

    html = f"""<!DOCTYPE html>
<html><head><meta charset='utf-8'><title>API Test Reports</title>
<style>
body{{font-family:Arial, sans-serif; background:#f9f9f9; padding:40px;}}
table{{margin:auto;border-collapse:collapse;width:80%;background:#fff}}
th,td{{border:1px solid #ccc;padding:10px;text-align:center}}
th{{background:#4CAF50;color:#fff}}
tr:hover{{background:#f1f1f1}}
</style>
</head>
<body>
<h1 style='text-align:center'>📈 API Test Reports</h1>
<p style='text-align:center;color:#777'>Generated {now}</p>
<table>
<thead><tr><th>Report</th><th>Link</th></tr></thead>
<tbody>
{rows}
</tbody>
</table>
</body></html>"""

    index_html.write_text(html, encoding="utf-8")
    # ensure .nojekyll
    (base_dir / ".nojekyll").touch(exist_ok=True)
    print(f"[INFO] Generated index.html with {len(report_files)} entries at root. Output dir: {output_dir_name}")

if __name__ == "__main__":
    main()
