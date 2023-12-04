from config.settings.base import DEBUG

if DEBUG:
    from config.settings.local import *
else:
    from config.settings.prod import *
