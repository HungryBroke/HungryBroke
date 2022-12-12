from .base import *  # noqa: F401, F403

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "hbdb",
        "USER": "hbpostgres",
        "PASSWORD": "hbpostgres",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
