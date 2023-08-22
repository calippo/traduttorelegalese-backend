test:
	curl http://0.0.0.0:8081/hello

test-deploy:
	curl https://legalese-backend.fly.dev/hello

file-test:
	curl -X POST -H "Authorization: Bearer 12345" -F "file=@test.docx" http://0.0.0.0:8081/upload

file-tedt-deploy:
	curl -X POST -H "Authorization: Bearer 12345" -F "file=@test.docx" https://legalese-backend.fly.dev/upload

run:
	poetry run python app/app.py

install:
	poetry install

build:
	docker build -t traduttorelegalese .

tag:
	docker tag traduttorelegalese ghcr.io/calippo/traduttorelegalese-backend:v2

push:
	docker push ghcr.io/calippo/traduttorelegalese-backend:v2
