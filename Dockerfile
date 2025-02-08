FROM python:3.12-slim-bullseye

# Set environment variable to avoid buffering of stdout/stderr
ENV PYTHONUNBUFFERED=1

# Create and set working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements.txt file into the container
COPY requirements.txt /code/

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Ensure start-django.sh is executable
RUN chmod +x /code/start-django.sh

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Django server when the container starts
ENTRYPOINT ["/code/start-django.sh"]
