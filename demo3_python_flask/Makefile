TAG := demo3-flask
APP_DIR := flask_app
APP_FILE_EXEC := main

build:

	docker build --network=host --build-arg APP_DIR=$(APP_DIR) --build-arg APP_FILE_EXEC=$(APP_FILE_EXEC) -t $(TAG) . 


run:

	docker run -it --network=host -v  $(shell pwd):/$(APP_DIR)  -p 5000:5000 $(TAG)