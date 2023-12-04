import os
from dotenv import load_dotenv

from django.core.exceptions import ImproperlyConfigured

# Load environment variables
load_dotenv()


def get_env_variable(var_name) -> str or Exception:
    """Get an environment variable or raise an exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the {} environment variable".format(var_name)
        raise ImproperlyConfigured(error_msg)


def get_bool_env(env_var) -> bool:
    """Parse 'boolean' environment variable strings."""
    return os.getenv(env_var, "False") == "True"
