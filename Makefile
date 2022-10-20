define help_msg

Usage:
	compile-requirements:    compile requirements in Docker
	run-project:             start project in Docker
	lint:                    format code with black and isort in local

endef
export help_msg

help:
	@echo "$$help_msg"

compile-requirements:
	docker-compose exec django pip-compile /app/requirements/base.in --upgrade

run-project:
	COLUMNS=150 DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose up --build

lint:
	python -m black backend --target-version py310
	python -m isort backend --profile=black
