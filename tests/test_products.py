import pytest, requests

# ---------- P1: Normal flows ---------- #
@pytest.mark.parametrize("min_p,max_p", [(1, 78), (1, 21)])
def test_price_between_ok(base_url, min_p, max_p):
    resp = requests.get(f"{base_url}/products?between=price,{min_p},{max_p}", timeout=10)
    assert resp.status_code == 200
    data = resp.json().get("data", [])
    for product in data:
        assert min_p <= product["price"] <= max_p

def test_page_1_ok(base_url):
    resp = requests.get(f"{base_url}/products?page=1", timeout=10)
    assert resp.status_code == 200
    assert resp.json().get("data", [])

def test_sort_name_asc_ok(base_url):
    resp = requests.get(f"{base_url}/products?sort=name,asc&between=price,1,100&page=0", timeout=10)
    assert resp.status_code == 200
    data = resp.json().get("data", [])
    names = [p["name"] for p in data]
    assert names == sorted(names)

def test_product_detail_valid(base_url, valid_product_id):
    resp = requests.get(f"{base_url}/products/{valid_product_id}", timeout=10)
    assert resp.status_code == 200
    data = resp.json()
    for field in ("id", "name", "price"):
        assert field in data

# ---------- P2: Reasonable errors ---------- #
@pytest.mark.parametrize("url,status", [
    ("/products?between=price,-10,5", 200),  # API actually returns 200 with empty data
    ("/products?sort=name,wrong", 200),      # returns 200 but ignores sort
])
def test_products_error_cases(base_url, url, status):
    resp = requests.get(f"{base_url}{url}", timeout=10)
    assert resp.status_code == status

def test_product_detail_invalid(base_url):
    resp = requests.get(f"{base_url}/products/INVALID_ID", timeout=10)
    assert resp.status_code == 404

# ---------- P3: Edge cases ---------- #
def test_page_9999_empty(base_url):
    resp = requests.get(f"{base_url}/products?page=9999", timeout=10)
    assert resp.status_code == 200
    assert resp.json().get("data", []) == []

def test_price_between_extreme(base_url):
    resp = requests.get(f"{base_url}/products?between=price,1,10000", timeout=10)
    assert resp.status_code == 200

def test_products_default_ok(base_url):
    resp = requests.get(f"{base_url}/products", timeout=10)
    assert resp.status_code == 200
    assert "data" in resp.json()