.EXPORT_ALL_VARIABLES:
.PHONY: venv help docker
# Unlike most variables, the variable SHELL is never set from the environment.
# This is because the SHELL environment variable is used to specify your personal
# choice of shell program for interactive use. It would be very bad for personal
# choices like this to affect the functioning of makefiles. See Variables from the Environment.
SHELL=/bin/bash
VIRTUAL_ENV=${PWD}/.venv
# LOCAL ENVIRONMENT
PYTHONUNBUFFERED=1

.ONESHELL:
venv:
	rm -rf $(VIRTUAL_ENV) && python3 -m venv $(VIRTUAL_ENV)
	$(VIRTUAL_ENV)/bin/pip3 install --upgrade pip wheel setuptools
	$(VIRTUAL_ENV)/bin/pip3 install --compile --upgrade --force-reinstall --requirement dev-requirements.txt

docker: docker.down docker.up

.ONESHELL:
docker.up:
	docker-compose -f dev-docker-compose.yml up --build -d

.ONESHELL:
docker.log:
	docker-compose -f dev-docker-compose.yml logs  --follow

.ONESHELL:
docker.stop:
	docker-compose -f dev-docker-compose.yml stop

.ONESHELL:
docker.down:
	docker-compose -f dev-docker-compose.yml down --volumes --rmi local  --remove-orphans

.ONESHELL:
flake8:
	$(VIRTUAL_ENV)/bin/flake8 src

.ONESHELL:
black:
	$(VIRTUAL_ENV)/bin/black --line-length 88 --pyi --skip-string-normalization --safe src

build: venv docker flake8 test run

.ONESHELL:
test:
	$(VIRTUAL_ENV)/bin/pytest src

.ONESHELL:
run:
	$(VIRTUAL_ENV)/bin/python src/app.py

build: venv docker flake8 test run

help:
	@echo "Usage:"
	@echo "  make venv - create virtual environment for the project"
	@echo "  make docker - run dev environment docker-compose"
	@echo "  make docker.up - dev environment docker-compose up"
	@echo "  make docker.stop - dev environment docker-compose stop"
	@echo "  make docker.log - dev environment docker-compose log"
	@echo "  make docker.down - dev environment docker-compose down"
	@echo "  make flake8 - run flake8 on the project"
	@echo "  make black - run black on the project"
	@echo "  make test - run automated tests"
	@echo "  make run - run server"
	@echo "  make build - build the project"
