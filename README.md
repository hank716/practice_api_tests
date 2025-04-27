# 🚀 Practice API Testing Framework

🔗 Lightweight project for API Automation Testing Practice using **Pytest**, **Postman**, and **Newman**.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)]()
[![Pytest](https://img.shields.io/badge/Pytest-8.1.1-brightgreen)]()
[![Postman Collection](https://img.shields.io/badge/Postman-Collection-orange)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey.svg)]()

---

## Table of Contents
- [📚 Tech Stack](#-tech-stack)
- [📂 Project Structure](#-project-structure)
- [🚀 Features](#-features)
- [⚙️ Installation](#-installation)
- [🧪 Test Execution](#-test-execution)
- [📊 Test Coverage Summary](#-test-coverage-summary)
- [🗓️ API Response Structures](#-api-response-structures)
- [📊 Reports](#-reports)
- [🔄 CI/CD Pipeline](#-cicd-pipeline)
- [📢 Notes](#-notes)
- [🎯 Author](#-author)

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 📚 Tech Stack

- **Language**: Python 3
- **Test Framework**: Pytest
- **HTTP Client**: Requests
- **API Collection Tool**: Postman + Newman
- **Report Generation**: pytest-html, newman-reporter-htmlextra, custom GitHub Pages index
- **Structure**: Modularized by API Features (Products, Messages)
- **CI/CD**: GitHub Actions (auto-run tests and publish reports)

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 📂 Project Structure

```
PRACTICE_API_TESTS/
🔘 collection/
    └️ PracticeSoftwareTesting_API_Collection.json
🔘 reports/
    └️ (Generated HTML reports here)
🔘 scripts/
    ├️ generate_index.py
    ├️ run_all_test.py
    ├️ run_newman.py
    └️ run_pytests.py
🔘 tests/
    ├️ test_products.py
    └️ test_messages.py
🔘 .github/workflows/
    └️ python-ci.yml
🔘 .gitignore
🔘 conftest.py
🔘 pytest.ini
🔘 requirements.txt
🔘 run.sh
🔘 Makefile
🔘 README.md
```

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🚀 Features

- ✅ Postman Collection Testing via Newman
- ✅ API Automation Testing with Pytest
- ✅ One-click Full Execution (Pytest + Newman)
- ✅ Timestamped HTML Reports
- ✅ Professional modular project layout
- ✅ GitHub Actions CI/CD pipeline integration
- ✅ GitHub Pages report auto-deployment

[🔝 Back to Top](#-practice-api-testing-framework)

---

## ⚙️ Installation

```bash
git clone https://github.com/hank716/practice_api_tests.git
cd practice_api_tests
```

Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Newman globally:

```bash
npm install -g newman newman-reporter-htmlextra
```

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🧪 Test Execution

### Run All Tests (bash script)

```bash
chmod +x run.sh
./run.sh
```

### Run with Makefile

| Command | Description |
|:--------|:------------|
| make all     | Run all tests (Pytest + Newman) |
| make pytest  | Run only Pytest |
| make newman  | Run only Newman |
| make clean   | Clean all caches and reports |

### Run individual scripts

```bash
python scripts/run_pytests.py
python scripts/run_newman.py
python scripts/run_all_test.py
```

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 📊 Test Coverage Summary

| # | Module | Description | Priority |
|---|--------|-------------|----------|
| 1 | Products | Search products between price 1-78 | P1 |
| 2 | Products | Paginate first page of products | P1 |
| 3 | Products | Search products between price 1-21 | P1 |
| 4 | Products | Sort products by name ascending | P1 |
| 5 | Products | Get product details by valid ID | P1 |
| 6 | Messages | Submit a message normally | P1 |
| 7 | Products | Validate response fields | P1 |
| 8 | Products | Validate price field type | P1 |
| 9 | Products | Query invalid product ID | P2 |
| 10 | Products | Search products with negative price range | P2 |
| 11 | Products | Query with invalid sort param | P2 |
| 12 | Messages | Submit missing email field | P2 |
| 13 | Messages | Submit invalid email format | P2 |
| 14 | Messages | Submit empty fields | P2 |
| 15 | Messages | Submit name with special characters | P3 |
| 16 | Products | Query with special sort characters | P3 |
| 17 | Products | Paginate non-existent high page | P3 |

✅ **Total: 17 Test Cases**

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🗓️ API Response Structures

### 🔵 GET /products

```json
{
  "current_page": 1,
  "data": [...],
  "from": 1,
  "last_page": 6,
  "per_page": 10,
  "to": 10,
  "total": 60
}
```

- **Pagination fields** included.
- **Data** is an array of product details.

### 🔸 GET /products/{product_id}

```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "price": 9.99,
  "is_location_offer": 1,
  "is_rental": 0,
  "in_stock": 0,
  "brand": {...},
  "category": {...},
  "product_image": {...}
}
```

### 🔹 POST /messages

```json
{
  "name": "string",
  "subject": "string",
  "message": "string",
  "email": "string@example.com"
}
```

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 📊 Reports

- All reports generated under `/reports/`
- HTML reports generated for:
  - Pytest
  - Newman
- Reports are timestamped and organized
- Auto-published via GitHub Actions to GitHub Pages
- Index page generated automatically by `generate_index.py`

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🔄 CI/CD Pipeline

✅ GitHub Actions (`.github/workflows/python-ci.yml`) automatically:
1. Set up Python environment.
2. Install project dependencies.
3. Run Pytest and generate HTML reports.
4. Run Newman and generate HTML reports.
5. Upload reports to `gh-pages` branch for GitHub Pages hosting.

Every push to `main` branch will:
- **Trigger automated API tests**
- **Generate fresh reports**
- **Deploy reports to a live GitHub Pages site**

> 📢 **Result:** Full test automation with instant feedback and online-accessible test results!

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🌐 GitHub Pages - Auto Publish Test Reports

### What is GitHub Pages?
GitHub Pages allows you to **host HTML reports directly from your repository**, making it easy to browse your test results online.

### How It Works

- Our **CI/CD workflow** automatically:
  1. Runs API tests (Pytest + Newman).
  2. Generates timestamped HTML reports.
  3. Commits generated reports to the `gh-pages` branch.
  4. Publishes `gh-pages` branch via GitHub Pages.

- The **`generate_index.py`** script creates a dynamic `index.html` that lists all report files for easy navigation.

### Setup Instructions (One-time)

1. Go to your repository **Settings** → **Pages**.
2. Under **Build and deployment**, set:
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages`
   - **Folder**: `/ (root)`
3. Save.

After this, every new test run will automatically update the report site!

### View the Reports

Once setup, you can view your API test reports at:

```
https://<your-github-username>.github.io/<your-repo-name>/
```

Example:

```
https://hank716.github.io/practice_api_tests/
```

You will see:
- ✅ Pytest HTML Report
- ✅ Newman HTML Report
- ✅ Auto-generated index.html linking all reports

> 🚀 **Result**: Test results become easily accessible online, no manual uploads needed!

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 📢 Notes

- Base URL: `https://api.practicesoftwaretesting.com`
- Test results printed to console during run.
- HTML Reports stored locally and published remotely.

[🔝 Back to Top](#-practice-api-testing-framework)

---

## 🎯 Author

- **Hank Wang**
- Personal project for API automation practice.

[🔝 Back to Top](#-practice-api-testing-framework)

---

# 🌟 Happy Testing!

[🔝 Back to Top](#-practice-api-testing-framework)

