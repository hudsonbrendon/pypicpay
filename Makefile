install:
	poetry run python setup.py install

isort:
	poetry run isort .

flake8:
	poetry run flake8 .

black:
	poetry run black . --check

coverage:
	poetry run coverage report -m

test:
	poetry run python tests/tests.py

dev:
	make install
	make isort
	make flake8
	make black
	make test