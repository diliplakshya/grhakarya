FROM python:3.11.1-slim-buster
# Make /app as a working directory in the container
WORKDIR /app

# set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Expose the port 5000 in which our application runs
EXPOSE 5000 
# Copy requirements from host, to docker container in /app 
# COPY ./requirements.txt .
# Install the dependencies
# RUN pip install --no-cache-dir --upgrade -r requirements.txt
ARG AWS_REGION
ARG AWS_ACCESS_KEY_ID
ARG AWS_SECRET_ACCESS_KEY
ARG SECRET_KEY
ARG ALGORITHM
ARG ACCESS_TOKEN_EXPIRE_MINUTES
ARG HASHED_PASSWORD
# Copy everything from ./src directory to /app in the container
COPY src /app/src
COPY __init__.py .
COPY Dockerfile .
COPY pyproject.toml .

RUN pip3 install poetry
# already in a virtual environment by using a docker image, there's no need to build another environment
RUN poetry config virtualenvs.create false

# Installs all the required packages minus the development packages
RUN poetry install --no-dev

# Run the application in the port 5000
CMD ["uvicorn", "src.main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "5000"]
