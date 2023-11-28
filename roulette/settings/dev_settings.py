import os

from .settings import (
    INSTALLED_APPS,
    MIDDLEWARE,
)

DEBUG = True

DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda _: True,
}

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(2, "debug_toolbar.middleware.DebugToolbarMiddleware")
