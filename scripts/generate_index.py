import datetime
from pathlib import Path

def generate_index_html():
    base_dir = Path(__file__).parent.parent
    gh_pages_dir = base_dir / "gh-pages"
    index_file = gh_pages_dir / "index.html"

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>API Test Reports</title>
    </head>
    <body>
        <h1>Test Reports (Generated {now})</h1>
        <ul>
    """

    for report in sorted(gh_pages_dir.glob("*.html")):
        if report.name != "index.html":
            html_content += f'<li><a href="{report.name}">{report.name}</a></li>\n'

    html_content += """
        </ul>
    </body>
    </html>
    """

    index_file.write_text(html_content, encoding="utf-8")
    print(f"[INFO] Generated {index_file}")

if __name__ == "__main__":
    generate_index_html()
