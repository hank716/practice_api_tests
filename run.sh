#!/bin/bash

echo "Running pytest tests..."
python scripts/run_pytests.py

echo "Running Postman Collection with newman..."
python scripts/run_newman.py

echo "All tests completed!"
