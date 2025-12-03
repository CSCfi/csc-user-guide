from os import getenv


if getenv("MKDOCS_ENV") == "production":
    from archives import *
