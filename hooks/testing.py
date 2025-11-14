from os import getenv


if getenv("MKDOCS_ENV") == "test":
    from testing import *
