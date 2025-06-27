#!/bin/bash

# UV Migration Script for AI Concierge Project

echo "🚀 AI Concierge UV Migration Script"
echo "======================================"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "📦 Installing uv..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source $HOME/.cargo/env
else
    echo "✅ uv is already installed"
fi

# Initialize uv project if not exists
if [ ! -f "pyproject.toml" ]; then
    echo "🔧 Initializing uv project..."
    uv init --no-readme
fi

# Sync dependencies
echo "📥 Installing dependencies with uv..."
uv sync

# Generate lock file
echo "🔒 Generating lock file..."
uv lock

echo "✅ Migration complete!"
echo ""
echo "📋 Next steps:"
echo "1. Run the app: uv run uvicorn api.main:app --reload"
echo "2. Run tests: uv run pytest"
echo "3. Build Docker: docker build -t ai-concierge ."
echo ""
echo "📖 See UV_COMMANDS.md for more uv usage examples"
