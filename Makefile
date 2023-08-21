test:
	curl http://127.0.0.1:5000/hello

file-test:
	curl -X POST -F "file=@test.docx" http://127.0.0.1:5000/upload

run:
	poetry run python app/app.py

install:
	poetry install
