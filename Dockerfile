# Use Python 3.12.10 slim based on Debian Bookworm
FROM python:3.12.10-slim-bookworm

# Copy uv and uvx from the official uv image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /code

# Make the virtual environment available
ENV PATH="/code/.venv/bin:$PATH"

# Copy project configuration files
COPY pyproject.toml uv.lock .python-version README.md ./

# Copy application source code
COPY src ./src

# Install dependencies exactly from uv.lock
RUN uv sync --locked

# Expose FastAPI port
EXPOSE 9696

# Start FastAPI application
ENTRYPOINT ["uvicorn", "src.machine_learning_zoomcamp_2026_course_deployment_module_project.app:app", "--host", "0.0.0.0", "--port", "9696"]