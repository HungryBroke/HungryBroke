# All commands either run in docker or start in docker.

initialize-repository:
	# Steps to run before making your first commit
	pre-commit install --hook-type commit-msg --hook-type pre-push
	git update-index --assume-unchanged backend/.envs/.overrides


run-project:
	docker compose up --build

compile-requirements:
	docker compose exec django pip-compile /app/requirements/base.in --upgrade

bash:
	docker compose exec django bash


create-superuser:
	# Create a superuser, password is set through environment variable DJANGO_SUPERUSER_PASSWORD
	docker compose exec django python manage.py createsuperuser

create-migrations:
	docker compose exec django python manage.py makemigrations

migrate:
	docker compose exec django python manage.py migrate

quick-migrate: create-migrations migrate

test:
	docker compose exec -e "DJANGO_SETTINGS_MODULE=HungryBroke.settings.base" django pytest
