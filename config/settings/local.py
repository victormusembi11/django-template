from config.settings.base import *
from config.settings.utils import get_env_variable

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DB_ENGINE = get_env_variable("DB_ENGINE")
DB_NAME = get_env_variable("DB_NAME")
DB_USER = get_env_variable("DB_USER")
DB_PASS = get_env_variable("DB_PASS")
DB_HOST = get_env_variable("DB_HOST")
DB_PORT = get_env_variable("DB_PORT")

DB_IS_AVAIL = all(
    [
        DB_ENGINE,
        DB_NAME,
        DB_USER,
        DB_PASS,
        DB_HOST,
        DB_PORT,
    ]
)

if DB_IS_AVAIL:
    DATABASES = {
        "default": {
            "ENGINE": DB_ENGINE,
            "NAME": DB_NAME,
            "USER": DB_USER,
            "PASSWORD": DB_PASS,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files (Images, Videos, etc.)
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"
