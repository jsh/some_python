# The usual

SOURCES := $(wildcard *.py)

all: lint

black:
	black -q ${SOURCES} ${TESTS}

clean:
	git clean -dfx ${NO_CLEAN:%=--exclude %}

isort:
	isort ${SOURCES} ${TESTS}

lint: black pylint

pylint:
	# pylint --rcfile=.config/pylint -rn ${SOURCES} ${TESTS} | sort -t: -k2 -n -r
	pylint -rn ${SOURCES} ${TESTS} | sort -t: -k2 -n -r

.PHONY: all black clean isort lint pylint
