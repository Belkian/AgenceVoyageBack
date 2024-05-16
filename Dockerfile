# Dockerfile for building a Python application image with mounted volume and exposed port 8080

# Use an official Python runtime as a base image
FROM python:3.12.2-slim

# Installing prerequisite packages
RUN DEBIAN_FRONTEND="noninteractive" apt-get update && apt-get install -y tzdata keyboard-configuration

# system settings
RUN apt-get install -y build-essential

# Set the working directory in the container to /app
WORKDIR /AgenceVoyage/core
# Assuming your codebase has a requirements.txt, install Python dependencies
# COPY ./AgenceVoyage /AgenceVoyage/
COPY requirements.txt /AgenceVoyage/core/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Keep the container running with a non-terminating command
# CMD ["tail", "-f", "/dev/null"]

CMD python manage.py runserver 