# UV Commands Reference for AI Concierge Project

## Installation
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Or with pip
pip install uv
```

## Project Setup
```bash
# Initialize project with uv
uv init

# Install dependencies
uv sync

# Add new dependency
uv add fastapi
uv add --dev pytest

# Remove dependency
uv remove package-name

# Update dependencies
uv sync --upgrade
```

## Development Commands
```bash
# Run the application
uv run uvicorn api.main:app --reload

# Run tests
uv run pytest

# Run formatting
uv run black .
uv run isort .

# Run linting
uv run flake8 .
uv run mypy .

# Install development dependencies
uv sync --group dev
```

## Docker with UV
```bash
# Build Docker image with uv
docker build -t ai-concierge .

# Build with conda fallback
docker build -f Dockerfile.conda -t ai-concierge-conda .

# Run container
docker run -p 8000:8000 ai-concierge
```

## Lock Files
```bash
# Generate lock file
uv lock

# Install from lock file
uv sync --frozen

# Export to requirements.txt (for compatibility)
uv export --format requirements-txt --output-file requirements.txt
```

## Migration from pip/conda
```bash
# Convert requirements.txt to pyproject.toml
uv init --from requirements.txt

# Install existing requirements
uv sync
```

## Performance Benefits
- **10-100x faster** than pip for dependency resolution
- **Cached downloads** for repeated builds
- **Parallel installation** of packages
- **Better conflict resolution**
