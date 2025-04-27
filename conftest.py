import os
import logging
from pathlib import Path
import requests
import pytest

# ──────────────────────────────────────────────
# Basic logging settings (INFO level, output to the terminal)
# run_tests.py will use --capture=tee-sys to write stdout to html synchronously
# ──────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)

# ─────────── General parameters / Fixtures ───────────
BASE_URL = os.getenv("BASE_URL", "https://api.practicesoftwaretesting.com")


@pytest.fixture(scope="session")
def base_url() -> str:
    """Base URL for all requests."""
    return BASE_URL


@pytest.fixture(scope="session")
def product_list(base_url):
    """
    Query the first page and cache result for the whole session.
    """
    resp = requests.get(f"{base_url}/products?page=1", timeout=10)
    if resp.status_code != 200:
        pytest.skip("Unable to fetch product list – skipping dependent tests.")
    return resp.json().get("data", [])


@pytest.fixture(autouse=True)
def log_request_response():
    """Auto-log every requests request + response status."""
    old_get = requests.get
    old_post = requests.post

    def _wrap(method, func):
        def inner(*args, **kwargs):
            logging.info("%s %s", method, args[0])
            resp = func(*args, **kwargs)
            logging.info("→ %s %s", method, resp.status_code)
            return resp
        return inner

    requests.get = _wrap("GET", old_get)
    requests.post = _wrap("POST", old_post)
    yield
    # restore
    requests.get, requests.post = old_get, old_post


@pytest.fixture(scope="session")
def valid_product_id(product_list):
    """
    Returns the first product id as a valid sample.
    """
    if not product_list:
        pytest.skip("Product list is empty – skipping tests that need a valid ID.")
    return product_list[0]["id"]


# ─────────── pytest-html hooks ───────────
try:
    import pytest_html
except ImportError: # pytest-html is not installed
    pytest_html = None


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Add metadata to pytest-html report (only if plugin is active).
    """
    if pytest_html and hasattr(config, "_metadata"):
        config._metadata.update({"Project": "Practice API Tests"})


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Attach captured stdout / log to the html report, even when a test PASSES.
    """
    outcome = yield
    report = outcome.get_result()

    if pytest_html is None or report.when != "call":
        return

    captured = getattr(report, "capstdout", "")
    caplog_text = getattr(report, "caplog", "")

    log_blocks = []
    if caplog_text:
        log_blocks.append("**Captured Log**\n```\n" + caplog_text.strip() + "\n```")
    if captured:
        log_blocks.append("**Captured Stdout**\n```\n" + captured.strip() + "\n```")

    if log_blocks:
        if not hasattr(report, "extra"):
            report.extra = []
        report.extra.append(pytest_html.extras.html("<br>".join(log_blocks)))
