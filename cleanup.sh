#!/bin/bash
# Cleanup script for CommonDataTypes project
# Removes temporary files, build artifacts, and cache directories

echo "🧹 Cleaning up temporary files and artifacts..."

# Python bytecode files
echo "📁 Removing Python bytecode files..."
find . -name "*.pyc" -not -path "./.venv/*" -type f -delete
find . -name "*.pyo" -not -path "./.venv/*" -type f -delete

# Python cache directories
echo "📁 Removing __pycache__ directories..."
find . -name "__pycache__" -not -path "./.venv/*" -type d -exec rm -rf {} + 2>/dev/null || true

# Build artifacts
echo "📁 Removing build artifacts..."
rm -rf build/
rm -rf dist/
rm -rf *.egg-info/

# Test and coverage artifacts
echo "📁 Removing test and coverage artifacts..."
rm -rf .pytest_cache/
rm -rf htmlcov/
rm -f .coverage
rm -f coverage.xml

# Linting and type checking cache
echo "📁 Removing linting and type checking cache..."
rm -rf .mypy_cache/
rm -rf .flake8_cache/

# IDE and OS artifacts
echo "📁 Removing IDE and OS artifacts..."
find . -name ".DS_Store" -type f -delete
find . -name "Thumbs.db" -type f -delete
find . -name "*.swp" -type f -delete
find . -name "*.swo" -type f -delete
find . -name "*~" -type f -delete

# Temporary files
echo "📁 Removing temporary files..."
find . -name "*.tmp" -type f -delete
find . -name "*.temp" -type f -delete
find . -name "*.log" -type f -delete

# Node.js artifacts (if any)
rm -rf node_modules/
rm -f package-lock.json
rm -f yarn.lock

echo "✅ Cleanup complete!"
echo "📊 Current directory size:"
du -sh . --exclude=.venv