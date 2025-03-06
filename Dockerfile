# Base stage for common setup
FROM python:3.12-slim-bullseye AS base

# Set environment variable to avoid buffering of stdout/stderr
ENV PYTHONUNBUFFERED=1

# Create and set working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements files into the container
COPY requirements.txt /code/
COPY requirements-dev.txt /code/

# Install production dependencies by default
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Ensure start-django.sh is executable
RUN chmod +x /code/start-django.sh

# Expose the port the app runs on
EXPOSE 8000

# Dev stage - this is the default one we'll use for development
FROM base AS dev

# Install development dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Define ENTRYPOINT to start the Django server (Development)
ENTRYPOINT ["/code/start-django.sh"]

# Prod stage
FROM base AS prod

# Install only production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure prod-specific files and optimizations (skip Playwright in prod)
RUN python manage.py collectstatic --no-input

# Command to run the Django server when the container starts (Production)
ENTRYPOINT ["/code/start-django.sh"]
