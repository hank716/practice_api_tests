import datetime
from pathlib import Path

def generate_index_html():
    base_dir = Path(__file__).parent.parent
    gh_pages_dir = base_dir / "gh-pages"
    index_file = gh_pages_dir / "index.html"

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API Test Reports</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
    <div class="container">
        <h1 class="mb-4">All API Test Reports</h1>
        <p>Generated at: {now}</p>
        <ul class="list-group">
    """

    for folder in sorted(gh_pages_dir.iterdir()):
        if folder.is_dir():
            html_content += f'<li class="list-group-item"><a href="{folder.name}/">{folder.name}</a></li>\n'

    html_content += """
        </ul>
    </div>
</body>
</html>"""

    index_file.write_text(html_content, encoding="utf-8")
    print(f"[INFO] Generated {index_file}")

if __name__ == "__main__":
    generate_index_html()
