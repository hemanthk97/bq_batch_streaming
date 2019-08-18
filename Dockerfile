FROM python:3-slim


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install google-cloud-bigquery

# Run app.py when the container launches
CMD ["python", "test2.py"]
