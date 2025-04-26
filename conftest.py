import os, pytest, requests

BASE_URL = os.getenv("BASE_URL", "https://api.practicesoftwaretesting.com")

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def product_list(base_url):
    resp = requests.get(f"{base_url}/products?page=1", timeout=10)
    if resp.status_code != 200:
        pytest.xfail("Cannot fetch product list")
    return resp.json().get("data", [])

@pytest.fixture(scope="session")
def valid_product_id(product_list):
    if not product_list:
        pytest.xfail("Product list empty")
    return product_list[0]["id"]