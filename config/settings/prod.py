import dj_database_url
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from config.settings.base import *
from config.settings.utils import get_env_variable

INSTALLED_APPS += [
    "storages",
]

ALLOWED_HOSTS = get_env_variable("ALLOWED_HOSTS").split(",")

# Append WhiteNoise middleware to the top of the middleware list.
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(
        default=get_env_variable("DATABASE_URL"),
        conn_max_age=600,
        conn_health_checks=True,
    )
}

sentry_sdk.init(
    dsn=get_env_variable("SENTRY_DSN"),
    traces_sample_rate=1.0,
    profiles_sample_rate=1.0,
    enable_tracing=True,
    integrations=[
        DjangoIntegration(
            transaction_style="url",
            middleware_spans=True,
            signals_spans=True,
            cache_spans=True,
        ),
    ],
)

# AWS S3 settings for static files storage and serving.
# https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html

AWS_ACCESS_KEY_ID = get_env_variable("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = get_env_variable("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = get_env_variable("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = get_env_variable("AWS_S3_SIGNATURE_NAME")
AWS_S3_REGION_NAME = get_env_variable("AWS_S3_REGION_NAME")
AWS_S3_FILE_OVERWRITE = get_bool_env("AWS_S3_FILE_OVERWRITE")
AWS_DEFAULT_ACL = get_bool_env("AWS_DEFAULT_ACL")
AWS_S3_VERITY = get_bool_env("AWS_S3_VERITY")

AWS_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = f"https://{AWS_CUSTOM_DOMAIN}/static/" if DEBUG else "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]

# Media files (Images, Videos, etc.)
# https://docs.djangoproject.com/en/4.2/topics/files/

MEDIA_URL = f"https://{AWS_CUSTOM_DOMAIN}/media/" if DEBUG else "/media/"

MEDIA_ROOT = BASE_DIR / "media"
