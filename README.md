# Pytest - Write A TestCase

[![Python Tests](https://github.com/novalrizkyangkasa/Pytest-Write_A_TestCase/actions/workflows/python-tests.yml/badge.svg?branch=main)](https://github.com/novalrizkyangkasa/Pytest-Write_A_TestCase/actions/workflows/python-tests.yml)

Simple Python project for learning how to write test cases with `pytest`.

## 1. Setup / Installation (Python and Pytest)

### Prerequisites
- Python 3.10+ installed
- `pip` available

### Install steps
```bash
# check python version
python3 --version

# create virtual environment
python3 -m venv .venv

# activate virtual environment (macOS/Linux)
source .venv/bin/activate

# activate virtual environment (Windows PowerShell)
# .venv\Scripts\Activate.ps1

# install pytest
pip install -U pip pytest
```

## 2. How to Clone or Import

### Clone from GitHub
```bash
git clone git@github.com:novalrizkyangkasa/Pytest-Write_A_TestCase.git
cd Pytest-Write_A_TestCase
```

Alternative (HTTPS):
```bash
git clone https://github.com/novalrizkyangkasa/Pytest-Write_A_TestCase.git
cd Pytest-Write_A_TestCase
```

### Import existing project folder
- VS Code: `File` -> `Open Folder` -> select this project folder
- PyCharm: `Open` -> select this project folder

## 3. Project Structure

```text
Pytest-Write_A_TestCase/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── .gitignore
├── README.md
├── pytest.ini
├── test_math.py
├── calculate_total_price.py
├── apply_discount.py
└── validate_user_shipping_address.py
```

Additional local/generated directories:
- `.pytest_cache/`
- `__pycache__/`
- `.copy/`

## 4. GitHub Actions (Run Tests in GitHub)

GitHub Actions workflow file:
- `.github/workflows/python-tests.yml`

It runs tests automatically on:
- `push` to `main`
- `pull_request` to `main`
- manual trigger (`workflow_dispatch`)

Default version for auto run:
- Python `3.12`

### Run tests manually from GitHub UI
1. Open `Actions` tab in this repository.
2. Click workflow `Python Tests`.
3. Click `Run workflow`.
4. Choose `python_version` (`3.10` / `3.11` / `3.12`).
5. Select branch `main`, then click `Run workflow`.

### Run workflow from fork (for non-collaborator users)
1. Open this repository page.
2. Click `Fork` (top-right) and create fork in your account.
3. Open your fork repository.
4. Go to `Actions` tab.
5. If prompted, click `I understand my workflows, go ahead and enable them`.
6. Click workflow `Python Tests`.
7. Click `Run workflow`, choose `python_version`, then run.

Workflow artifacts per run:
- `test-reports-py<version>`
- contains `junit-<version>.xml` and `report-<version>.html`

Direct link:
- `https://github.com/novalrizkyangkasa/Pytest-Write_A_TestCase/actions/workflows/python-tests.yml`

## 5. How to Run (Local)

This project uses `pytest.ini` as default config:
```ini
[pytest]
addopts = -v -s
python_files = test_*.py *_test.py calculate_total_price.py apply_discount.py validate_user_shipping_address.py
```

### Run all tests (recommended)
```bash
pytest
```
This will automatically:
- use verbose mode (`-v`)
- show `print()` output (`-s`)
- discover all 4 test files above

Current result in this repo:
```bash
69 passed
```

### Run a specific file
```bash
pytest apply_discount.py
```

### Run tests filtered by keyword
```bash
pytest apply_discount.py -k invalid_code
```

### Run with explicit config file
```bash
pytest -c pytest.ini
```

## 6. Summary of Testcases in Each File

### `test_math.py` (8 test cases)
- `test_add_integers` (4): positive, mixed sign, zero, negative integers
- `test_add_floats` (4): positive, mixed sign, zero-like float, decimal precision with `pytest.approx`

### `calculate_total_price.py` (27 test cases)
- `test_calculate_cart_total_valid` (7): empty cart, single/multiple items, discount/no discount, full discount
- `test_calculate_cart_total_float_cases` (3): decimal price and decimal discount scenarios
- `test_invalid_structure_raises_value_error` (6): invalid container/type structure
- `test_calculate_cart_total_missing_keys` (6): missing `price`/`quantity` key scenarios
- `test_calculate_cart_total_non_numeric_values` (4): non-numeric price/quantity types
- `test_calculate_cart_total_default_discount` (1): default discount behavior

### `apply_discount.py` (25 test cases)
- `test_apply_discounts_normal_cases` (11): valid single/multiple discount codes, no discount, up to exact 100%
- `test_apply_discounts_float_cases` (5): float cart totals with different valid discount combinations
- `test_apply_discounts_invalid_code` (4): invalid code handling (`ValueError`)
- `test_apply_discounts_exceed_100_percent` (5): total discount above 100% (`ValueError`)

### `validate_user_shipping_address.py` (9 test cases)
- `test_validate_shipping_address_valid` (1): valid complete address
- `test_validate_shipping_address_invalid_type` (1): non-dictionary address input
- `test_validate_shipping_address_missing_fields` (7): single/multiple/all required fields missing
