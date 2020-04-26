install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

check: lint test
