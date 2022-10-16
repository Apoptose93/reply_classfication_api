build:
	docker build -t insta-classifier .
start:
	docker run -p 8000:8000 insta-classifier
