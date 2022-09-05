from base import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "hbdb",
        "USER": "hbpostgres",
        "PASSWORD": "hbpostgres",
        "HOST": "postgres",
        "PORT": "127.0.0.1",
    }
}
