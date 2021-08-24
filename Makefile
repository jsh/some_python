# The usual

PYTEST_OPTIONS := -q --doctest-modules
PYTHON_EXECUTABLE := $(shell which python3)
SOURCES := $(wildcard *.py)
TESTS := $(wildcard t/*.py)


all: black lint test

black: isort
	black -q ${SOURCES} ${TESTS}

clean:
	git clean -dfx ${NO_CLEAN:%=--exclude %}

coverage:
	- pytest ${PYTEST_OPTIONS} --cov="." --cov-report=html
	open htmlcov/index.html

isort:
	isort ${SOURCES} ${TESTS}

lint: pylint mypy

mypy:
	mypy --python-executable ${PYTHON_EXECUTABLE} $$PWD

pylint:
	pylint -rn ${SOURCES} ${TESTS} | sort -t: -k2 -n -r

pytest test:
	pytest ${PYTEST_OPTIONS}

.PHONY: all black clean coverage isort lint mypy pylint pytest test
