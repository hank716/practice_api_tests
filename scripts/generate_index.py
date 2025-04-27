from pathlib import Path
import datetime

def main():
    gh_pages_dir = Path(__file__).parent.parent / "gh-pages"
    index_html = gh_pages_dir / "index.html"
    gh_pages_dir.mkdir(parents=True, exist_ok=True)

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Scan all .html files (excluding index.html), sorted by modify time
    report_files = sorted([f for f in gh_pages_dir.glob("*.html") if f.name != "index.html"], key=lambda x: x.stat().st_mtime, reverse=True)

    table_rows = ""
    for report in report_files:
        filename = report.name
        title = filename.replace("_", " ").replace(".html", "").title()
        table_rows += f"""
        <tr>
            <td>{title}</td>
            <td><a href="{filename}" target="_blank">View Report</a></td>
        </tr>
        """

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>PracticeSoftwareTesting - API Test Reports</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; background-color: #f9f9f9; }}
            h1 {{ text-align: center; }}
            p {{ text-align: center; color: #888; }}
            table {{ margin: auto; width: 80%; border-collapse: collapse; background-color: #fff; }}
            th, td {{ padding: 12px 20px; border: 1px solid #ddd; text-align: center; }}
            th {{ background-color: #4CAF50; color: white; }}
            tr:hover {{ background-color: #f1f1f1; }}
            a {{ text-decoration: none; color: #2196F3; }}
        </style>
    </head>
    <body>
        <h1>📈 PracticeSoftwareTesting - API Test Reports</h1>
        <p>Generated on {now}</p>
        <table>
            <thead>
                <tr>
                    <th>Report Name</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody>
                {table_rows}
            </tbody>
        </table>
    </body>
    </html>
    """

    index_html.write_text(html_content.strip(), encoding="utf-8")
    print(f"[INFO] Generated index.html with {len(report_files)} reports.")

if __name__ == "__main__":
    main()
