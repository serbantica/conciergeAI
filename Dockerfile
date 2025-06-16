FROM continuumio/miniconda3

# Set working directory
WORKDIR /app

# Copy environment file and install dependencies
COPY concierge.yml .
RUN conda env create -f concierge.yml

# Make RUN commands use the new environment
SHELL ["conda", "run", "-n", "concierge", "/bin/bash", "-c"]

# Copy app code
COPY . .

# Expose port for FastAPI/Uvicorn
EXPOSE 8000

# Default command
CMD ["conda", "run", "-n", "concierge", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]