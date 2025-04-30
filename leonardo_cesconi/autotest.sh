#!/bin/bash

cd "$(dirname "$0")"

echo "Running Tests..."
make test

echo "Formatting with Black..."
make format

echo "Running Lint Checks..."
make lint

echo "All checks completed."
