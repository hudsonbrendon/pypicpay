install:
	pipenv run python setup.py install

isort:
	pipenv run isort .

flake8:
	pipenv run flake8 .

black:
	pipenv run black . --check

coverage:
	pipenv run coverage report -m

test:
	pipenv run python tests/tests.py

dev:
	make install
	make isort
	make flake8
	make black
	make test