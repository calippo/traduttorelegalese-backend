test:
	curl http://0.0.0.0:8081/hello

file-test:
	curl -X POST -H "Authorization: Bearer 12345" -F "file=@test.docx" http://0.0.0.0:8081/upload

run:
	poetry run python app/app.py

install:
	poetry install
