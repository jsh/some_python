# The usual

PYTEST_OPTIONS := -q --doctest-modules
SOURCES := $(wildcard *.py)
TESTS := $(wildcard t/*.py)

all: lint test

black: isort
	black -q ${SOURCES} ${TESTS}

clean:
	git clean -dfx ${NO_CLEAN:%=--exclude %}

coverage:
	- pytest ${PYTEST_OPTIONS} --cov="." --cov-report=html
	open htmlcov/index.html

isort:
	isort ${SOURCES} ${TESTS}

lint: black pylint

pylint:
	pylint -rn ${SOURCES} ${TESTS} | sort -t: -k2 -n -r

pytest test:
	pytest ${PYTEST_OPTIONS}

.PHONY: all black clean coverage isort lint pylint pytest test
