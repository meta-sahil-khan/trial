# Development stage
FROM python:alpine AS development

WORKDIR /python-docker

# Copy the requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy the application code
COPY . .
RUN ls


# Create a new user with UID 10016
RUN addgroup -g 10016 choreo && \
    adduser  --disabled-password  --no-create-home --uid 10016 --ingroup choreo choreouser

# Switch to the new user
USER 10016

EXPOSE 8000

# Start the Flask application
CMD ["python", "secA.py"]