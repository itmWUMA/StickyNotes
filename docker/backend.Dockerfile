# Use an official Python runtime as a parent image
FROM python:3.12

# Define build argument for pip index URL
ARG PIP_INDEX_URL

# Set the working directory in the container
WORKDIR /app/backend

# Copy the current directory contents into the container at /app/backend
COPY backend/requirements.txt .
COPY backend/app.py .

# Install any needed packages specified in requirements.txt, using the provided index URL if available
RUN pip install --no-cache-dir -r requirements.txt $(test -n "$PIP_INDEX_URL" && echo "--index-url $PIP_INDEX_URL")

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]