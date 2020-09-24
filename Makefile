install:
	poetry install

build:
	poetry build

publish:
	poetry publish --repository testpypi

lint:
	poetry run flake8 gendiff

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

check: lint test
