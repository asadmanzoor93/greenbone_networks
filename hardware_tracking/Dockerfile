# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory within the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container
COPY . /app/

# Expose the port the app runs
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Apply database migrations
RUN python manage.py migrate

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
