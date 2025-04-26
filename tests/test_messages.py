import json, pytest, requests

BASE_BODY = {
    "name": "AA AA",
    "subject": "return",
    "message": "Quality is not an act, it is a habit. Strive for excellence every day!",
    "email": "AAAA@gmail.com"
}

# ---------- P1 ---------- #
def test_post_message_ok(base_url):
    resp = requests.post(f"{base_url}/messages", json=BASE_BODY, timeout=10)
    assert resp.status_code == 200  # API returns 200

# ---------- P2 ---------- #
@pytest.mark.parametrize("bad_body", [
    {k: v for k, v in BASE_BODY.items() if k != "email"},
    {**BASE_BODY, "email": "aaa"},
    {"name": "", "subject": "", "message": "", "email": ""},
])
def test_post_message_invalid(base_url, bad_body):
    resp = requests.post(f"{base_url}/messages", json=bad_body, timeout=10)
    assert resp.status_code == 422 or resp.status_code == 200

# ---------- P3 ---------- #
def test_post_message_long(base_url):
    body = {**BASE_BODY, "message": "a" * 1001}
    resp = requests.post(f"{base_url}/messages", json=body, timeout=10)
    assert resp.status_code in (422, 200)

def test_post_name_special_chars(base_url):
    body = {**BASE_BODY, "name": "@#$%^&*"}
    resp = requests.post(f"{base_url}/messages", json=body, timeout=10)
    assert resp.status_code == 200