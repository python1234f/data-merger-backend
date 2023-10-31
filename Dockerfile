# Use an official Python runtime as the base image for the builder
FROM python:3.10-slim as builder

WORKDIR /app

# Install system packages required for compilation
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --user -r requirements.txt

# Production stage
FROM python:3.10-slim as runner

WORKDIR /app

# Copy the installed packages from the builder stage
COPY --from=builder /root/.local /root/.local

# Make sure scripts in .local are usable
ENV PATH=/root/.local/bin:$PATH

# Copy the project files to the container
COPY . /app/

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8888"]
