# All commands either run in docker or start in docker.

compile-requirements:
	docker-compose exec django pip-compile /app/requirements/base.in --upgrade

run-project:
	COLUMNS=150 DOCKER_BUILDKIT=1 COMPOSE_DOCKER_CLI_BUILD=1 docker-compose up --build

initialize-repository:
	# Steps to run before making your first commit
	pre-commit install --hook-type commit-msg --hook-type pre-push
	git update-index --assume-unchanged backend/.envs/.overrides

bash:
	docker-compose exec django bash

create-superuser:
	# Create a superuser, password is set through environment variable DJANGO_SUPERUSER_PASSWORD
	docker-compose exec django python manage.py createsuperuser
