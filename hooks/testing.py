from os import getenv


if getenv("PROPERDOCS_ENV") == "test":
    from testing import *
