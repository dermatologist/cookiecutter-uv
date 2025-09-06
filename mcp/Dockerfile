# Use an official Python runtime as a parent image
FROM python:3.12-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -e .

# Expose the port the MCP server listens on (e.g., 5000)
EXPOSE 5000

# Define the command to run the MCP server
CMD ["your-package-name"]