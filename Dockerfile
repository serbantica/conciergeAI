# Use official Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

# Set working directory
WORKDIR /app

# Install uv if not pre-installed
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock* ./

# Install dependencies using uv (much faster than pip)
RUN uv sync --frozen --no-cache

# Copy application code
COPY . .

# Expose port for FastAPI/Uvicorn
EXPOSE 8000

# Set environment variables
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH="/app"

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Default command using uv to run the application
CMD ["uv", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]