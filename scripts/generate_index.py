import os
from pathlib import Path
import datetime

def main():
    reports_dir = Path(__file__).parent.parent / "reports"
    index_path = reports_dir / "index.html"

    # 確保 reports 資料夾存在
    reports_dir.mkdir(exist_ok=True)

    # 找出所有時間戳資料夾
    timestamps = sorted(
        [f.name for f in reports_dir.iterdir() if f.is_dir()],
        reverse=True
    )

    # 開始生成 HTML
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>API Test Reports</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body class="p-5">
    <h1>API Test Reports</h1>
    <p>Generated at: {}</p>
    <table class="table table-striped">
        <thead>
            <tr>
                <th>#</th>
                <th>Test Timestamp</th>
                <th>View Reports</th>
            </tr>
        </thead>
        <tbody>
""".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    # 加入每一個 timestamp 的超連結
    for idx, ts in enumerate(timestamps, 1):
        html_content += f"""
            <tr>
                <td>{idx}</td>
                <td>{ts}</td>
                <td><a class="btn btn-primary" href="{ts}/" target="_blank">View</a></td>
            </tr>
        """

    # 結尾
    html_content += """
        </tbody>
    </table>
</body>
</html>"""

    # 寫入 index.html
    index_path.write_text(html_content, encoding="utf-8")
    print(f"Generated index.html with {len(timestamps)} reports.")

if __name__ == "__main__":
    main()
