import os

DEV_ENV = bool(os.environ.get("DEV_ENV", False))

exec("from .settings import *")
if DEV_ENV:
    exec("from .dev_settings import *")
