install:
	poetry install

build:
	poetry build

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest gendiff tests

check: lint test