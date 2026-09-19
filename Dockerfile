#Light python image
FROM python:3.11-slim

# Prevent Python from buffering stdout/stderr CHECK
ENV PYTHONUNBUFFERED=1

#Working directory
WORKDIR /app

# Copy requirements and application code
COPY collector.py /app/collector.py

# Create an unprivileged user for container security
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

ENTRYPOINT ["python", "-u", "/app/collector.py"]
