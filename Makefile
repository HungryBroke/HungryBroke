# All commands either run in docker or start in docker.

compile-requirements:
	docker-compose exec django pip-compile /app/requirements/base.in --upgrade

run-project:
	COLUMNS=160 DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose up --build
