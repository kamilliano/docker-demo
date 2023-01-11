TAG := demo2-python

build-good:

	docker build -t $(TAG) . -f Dockerfile.good


build-bad:

	docker build -t $(TAG) . -f Dockerfile.bad


run:
	# run this first for demo - demonstrate that you need to rebuild a container if you need to make changes
	docker run -it $(TAG)


run-with-volume:

	docker run -it -v $(shell pwd):/my_app $(TAG)