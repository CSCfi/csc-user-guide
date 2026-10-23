import os


if os.getenv("PROPERDOCS_ENV") in ["production", "staging"]:
    from archives import *
