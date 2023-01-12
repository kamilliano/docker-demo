# get base from https://hub.docker.com/_/python
FROM python:3.9.15-slim-buster

ARG APP_DIR=/flask_app
WORKDIR ${APP_DIR}

# Copy any application code that you want to install/run and bake it into the image
COPY Pipfile* .

RUN pip install pipenv && pipenv install --system

# Copy the rest of the files - discuss this on demo
COPY . .

# This is a default instruction that will be called during 'docker run'
CMD ["python", "main.py"]