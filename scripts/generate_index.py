import datetime
from pathlib import Path

def main():
    gh_pages_dir = Path(__file__).parent.parent / "gh-pages"
    folders = sorted(
        [f for f in gh_pages_dir.iterdir() if f.is_dir() and f.name not in [".git", ".github", "gh-pages"]],
        reverse=True
    )

    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>API Test Reports</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="bg-light">
  <div class="container py-5">
    <h1 class="mb-4">📊 API Test Reports</h1>
    <p>Generated at: {now}</p>
    <table class="table table-striped">
      <thead>
        <tr>
          <th>#</th><th>Test Timestamp</th><th>View Reports</th>
        </tr>
      </thead>
      <tbody>
"""

    for idx, folder in enumerate(folders, 1):
        folder_name = folder.name
        html += f"""
          <tr>
            <td>{idx}</td>
            <td>{folder_name}</td>
            <td><a class="btn btn-primary btn-sm" href="{folder_name}/index.html" target="_blank">View</a></td>
          </tr>
        """

    html += """
      </tbody>
    </table>
  </div>
</body>
</html>
"""

    (gh_pages_dir / "index.html").write_text(html)
    print(f"[INFO] Updated gh-pages/index.html")

if __name__ == "__main__":
    main()
