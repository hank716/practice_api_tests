# Practice Software Testing - API Automation Tests
(updated to match latest API response format)

This project automates the API test cases designed for the [PracticeSoftwareTesting](https://api.practicesoftwaretesting.com) sample system.  
It covers normal flows (P1), validation errors (P2), and edge cases (P3) through automated pytest scripts.

## 📚 Tech Stack
- Language: **Python 3**
- Test Framework: **pytest**
- HTTP Client: **requests**
- Structure: Modularized by API feature (`products`, `messages`)

## 🛠 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/hank716/practice_api_tests.git
   cd practice_api_tests
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 🚀 How to Run Tests

Run tests on default environment:

```bash
pytest -v
```

If you want to test against a different environment:

```bash
export BASE_URL=https://your-custom-env.com
pytest -v
```

Test results will display passed/failed status directly in the terminal.

---

## 📋 Test Coverage Overview

| # | Category | Test Description | Priority |
|---|----------|-------------------|----------|
| 1 | Products | Search products by price 1-78 | P1 |
| 2 | Products | Search products by price 1-21 | P1 |
| 3 | Products | Search products sorted by name ascending (price 1-100, page 0) | P1 |
| 4 | Products | View product details (valid ID) | P1 |
| 5 | Messages | Submit a valid message | P1 |
| 6 | Products | Search products by negative price -10~5 | P2 |
| 7 | Products | Search products with invalid sort parameter | P2 |
| 8 | Products | View product details with invalid ID | P2 |
| 9 | Messages | Submit message missing email field | P2 |
|10 | Messages | Submit message with incorrect email format | P2 |
|11 | Messages | Submit message with all fields blank | P2 |
|12 | Products | Search page 9999 | P3 |
|13 | Products | Search products with extreme price 1~10000 | P3 |
|14 | Products | Search products with special characters in sort param | P3 |
|15 | Messages | Submit message exceeding 1000 characters | P3 |
|16 | Messages | Submit name with special characters | P3 |
|17 | Products | Search products without any query parameters | P3 |

---

## 📁 Project Folder Structure

The project structure is organized as follows:

```
practice_api_tests/
├── README.md                         # Project introduction and instructions
├── requirements.txt                  # Python dependency list
├── pytest.ini                        # Pytest configuration
├── .gitignore                        # Git ignore rules
├── conftest.py                       # Common fixtures for tests
├── PracticeSoftwareTesting_Postman_Collection.json   # Postman collection for manual API testing
├── tests/                            # Folder containing automated test scripts
│   ├── test_products.py              # Tests for Products API
│   └── test_messages.py              # Tests for Messages API
└── assets/ (optional)                # (If present) Project banner image or other media assets
    └── banner.png                    # Project header banner
```

✅ This structure keeps manual testing and automation testing together, ensuring the project is easy to navigate and maintain.

---

## 🗂 API Response Structure

This section summarizes the expected JSON response structures for the Practice Software Testing API.

### 🔵 `GET /products`
Returns a paginated list of products.

**Response format:**
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
- **Important field:** `data` is the array containing the list of product objects.
- **Pagination fields:** `current_page`, `last_page`, `total`, etc., help in navigating through the list.

### 🟠 `GET /products/{product_id}`
Returns the details of a single product.

**Response format:**
```json
{
  "id": "string",
  "name": "string",
  "description": "string",
  "price": 9.99,
  "brand": { ... },
  "category": { ... },
  "product_image": { ... }
}
```
- The object contains all the detailed information about the selected product.

### 🟡 `POST /messages`
Submits a user message.

**Request format:**
```json
{
  "name": "string",
  "subject": "string",
  "message": "string",
  "email": "string"
}
```

**Typical server responses:**
- `201 Created` (original expectation) or
- `200 OK / 422 Unprocessable Entity` depending on input validation.

---

## 📌 Notes

- Default base URL: `https://api.practicesoftwaretesting.com`
- Some tests expect `valid_product_id` to be retrievable from the first page of `/products`.
- All requests have a timeout of 10 seconds.
- Test priorities are categorized as:
  - **P1**: Core normal flows
  - **P2**: Reasonable invalid flows (validation errors)
  - **P3**: Edge or extreme conditions