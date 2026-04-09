# Use the official Python runtime image + slim makes the image smaller
FROM python:3.12-slim
 
# Set environment variables 
# turns off an automatic check for pip updates each time
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
# Prevents Python from writing pyc files to disk
ENV PYTHONDONTWRITEBYTECODE=1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED=1 

# Set the working directory inside the container
WORKDIR /code
 
# Upgrade pip
RUN pip install --upgrade pip 
 
# Copy the Django project and install dependencies
COPY requirements.txt  /code/
RUN pip install --no-cache-dir -r requirements.txt


# Copy the Django project to the container
COPY . .
 