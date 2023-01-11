
hello-world:
	# Run example container from dockerhub: https://hub.docker.com/_/hello-world

	# Source code: https://github.com/docker-library/hello-world

	docker run --rm hello-world



hello-world-from-ubuntu:
	# Run a custom command by piping a string to bash, as an examples
	# can run any command 'lsb_release -a', 'cat /etc/os-release', 'env' etc
	docker run -it ubuntu bash -c "echo hello world"



list-images:
	# Get images that were build on our stystem
	docker images

inspect-image:

	docker image inspect $(IMAGE)


list-volumes:
	# list volumes on our system
	docker volume ls


inspect-volume:

	docker volume inspect $(VOLUME)


rm-all-docker-images:

	docker rmi -f $(shell docker images -aq)