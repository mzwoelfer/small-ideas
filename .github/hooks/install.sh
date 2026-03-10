#!/usr/bin/env bash
# Run once after cloning: bash .github/hooks/install.sh
set -e
cp .github/hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
echo "✓ pre-commit hook installed"
