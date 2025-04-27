
# 🚀 Practice API Testing Framework

🔗 Lightweight project for API Automation Testing Practice using **Pytest**, **Postman**, and **Newman**.

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)]()
[![Pytest](https://img.shields.io/badge/Pytest-8.1.1-brightgreen)]()
[![Postman Collection](https://img.shields.io/badge/Postman-Collection-orange)]()
[![License](https://img.shields.io/badge/License-MIT-lightgrey)]()

---

## 📚 Tech Stack

- **Language**: Python 3
- **Test Framework**: Pytest
- **HTTP Client**: Requests
- **API Collection Tool**: Postman + Newman
- **Report Generation**: pytest-html, newman-reporter-htmlextra
- **Structure**: Modularized by API Features (Products, Messages)

---

## 📂 Project Structure

```
PRACTICE_API_TESTS/
├── collection/
│   └── PracticeSoftwareTesting_API_Collection.json    # Postman Collection for API tests
├── reports/
│   └── (Generated HTML reports are stored here)        # Test reports (pytest + newman)
├── scripts/
│   ├── run_all_test.py                                 # Script to run both Pytest and Newman tests together
│   ├── run_newman.py                                   # Script to run Postman Collection using Newman
│   └── run_pytests.py                                  # Script to run API tests using Pytest
├── tests/
│   ├── test_products.py                                # API test cases for Product-related endpoints
│   └── test_messages.py                                # API test cases for Message submission endpoint
├── .gitignore                                          # Ignore Python caches, venv, reports, etc.
├── conftest.py                                         # Global Pytest fixtures (e.g., base URL, product ID setup)
├── pytest.ini                                          # Pytest configuration file
├── requirements.txt                                   # Python dependencies
├── run.sh                                              # Bash script to execute full test pipeline (pytest + newman)
├── Makefile                                            # Makefile for easier CLI operations (make all / pytest / newman / clean)
└── README.md                                           # Project documentation

```

---

## 🚀 Features

- ✅ Postman Collection Testing via Newman
- ✅ API Automation with Pytest
- ✅ One-click Full Execution
- ✅ Reports generated with Timestamped Filenames
- ✅ Professional, modular project structure

---

## ⚙️ Installation

1. Clone this repository:

```bash
git clone [<repository-url>](https://github.com/hank716/practice_api_tests.git)
cd practice_api_tests
```

2. Create a Python virtual environment:

```bash
python -m venv venv
source venv/bin/activate    # For Mac/Linux
venv\Scripts\activate     # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Newman globally:

```bash
npm install -g newman newman-reporter-htmlextra
```

---

## 🧪 Test Execution

### Run All Tests (bash script)

```bash
chmod +x run.sh
./run.sh
```

### Run with Makefile

```bash
make all
```

| Command | Description |
|:--------|:------------|
| `make all`     | Run all tests (Pytest + Newman) |
| `make pytest`  | Run only Pytest |
| `make newman`  | Run only Newman |
| `make clean`   | Clean all caches and reports |

### Run individual scripts

```bash
python scripts/run_pytests.py
python scripts/run_newman.py
python scripts/run_all_test.py
```

---

## 📈 Test Coverage Summary

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

---

## 📋 API Response Structures

### 🔵 GET `/products`

Returns a paginated list of products.

```json
{
  "current_page": 1,
  "data": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "price": 9.99,
      "is_location_offer": 1,
      "is_rental": 0,
      "in_stock": 0,
      "brand": {
        "id": "string",
        "name": "string",
        "slug": "string"
      },
      "category": {
        "id": "string",
        "parent_id": "string",
        "name": "string",
        "slug": "string",
        "sub_categories": [
          "string"
        ]
      },
      "product_image": {
        "by_name": "string",
        "by_url": "string",
        "source_name": "string",
        "source_url": "string",
        "file_name": "string",
        "title": "string",
        "id": "string"
      }
    }
  ],
  "from": 1,
  "last_page": 6,
  "per_page": 10,
  "to": 10,
  "total": 60
}
```

- **Important**: `data` array contains the products.
- **Pagination**: Includes `current_page`, `last_page`, `per_page`, `total`.

### 🟠 GET `/products/{product_id}`

Returns details of a single product.

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

### 🟡 POST `/messages`

Submit a message.

```json
{
  "name": "string",
  "subject": "string",
  "message": "string",
  "email": "string@example.com"
}
```

---

## 📊 Reports

- All generated under `/reports/`
- Separate HTML reports for Pytest and Newman
- Timestamped filenames for easy tracking

---

## 📢 Notes

- Base URL: `https://api.practicesoftwaretesting.com`
- Live execution progress shown in terminal.

---

## 🎯 Author

Hank Wang
Practice project for API Automation learning.

---

# 🌟 Happy Testing!
