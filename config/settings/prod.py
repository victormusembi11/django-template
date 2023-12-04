import dj_database_url

from config.settings.base import *
from config.settings.utils import get_env_variable

ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(",")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=get_env_variable("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}
