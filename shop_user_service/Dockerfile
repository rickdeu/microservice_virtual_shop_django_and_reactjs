# Use the official Python 3.9.5 image as the parent image
FROM python:3.9.5

# Set an environment variable to ensure that Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# Set the working directory to /shop_user_service within the container
WORKDIR /shop_user_service

# Copy the requirements.txt file to the container at /shop_user_service/requirements.txt
COPY shop_user_service/requirements.txt /shop_user_service/requirements.txt

# Install the Python dependencies specified in the requirements.txt file
RUN pip install -r requirements.txt

# Copy the rest of the application code to the container at /shop_user_service
COPY . /shop_user_service

# CMD specifies the default command to run when the container starts
# For a Python application, you would typically use a command like "python manage.py runserver"
# However, the CMD is commented out here, which means that the container will use the default CMD from the base image.
# You can uncomment and modify the CMD to match the command needed to run your specific Python application.
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
