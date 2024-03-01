#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull shubham1204pandey/flask-automation

# Run the Docker image as a container
docker run -d -p 5000:5000 shubham1204pandey/flask-automation
