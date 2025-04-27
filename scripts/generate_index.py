from pathlib import Path
import datetime

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
    <style>
        body {{
            padding: 3rem;
            background-color: #f8f9fa;
        }}
        .container {{
            max-width: 900px;
        }}
        .table thead th {{
            background-color: #343a40;
            color: white;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1 class="mb-4 text-center">📊 API Test Reports</h1>
        <p class="text-center text-muted">Generated at: {now}</p>
        <table class="table table-hover mt-4">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Test Timestamp</th>
                    <th scope="col">View Reports</th>
                </tr>
            </thead>
            <tbody>
    """

    folders = sorted([f for f in gh_pages_dir.iterdir() if f.is_dir()])
    for idx, folder in enumerate(folders, start=1):
        folder_name = folder.name
        html_content += f"""
                <tr>
                    <th scope="row">{idx}</th>
                    <td>{folder_name}</td>
                    <td><a href="{folder_name}/" class="btn btn-primary btn-sm" target="_blank">View</a></td>
                </tr>
        """

    html_content += """
            </tbody>
        </table>
    </div>
</body>
</html>"""

    index_file.write_text(html_content, encoding="utf-8")
    print(f"[INFO] Generated {index_file}")

if __name__ == "__main__":
    generate_index_html()
