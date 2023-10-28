# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download en_core_web_sm

# Expose the port Gunicorn will listen on (default is 8000)
EXPOSE 8080

# Define the command to run your application using Gunicorn
CMD ["gunicorn", "--workers=4", "--bind", "0.0.0.0:8080", "wsgi:app"]