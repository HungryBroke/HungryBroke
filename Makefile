# All commands either run in docker or start in docker.

compile-requirements:
	docker-compose exec django pip-compile /app/requirements/base.in --upgrade