from os import getenv


env = getenv("MKDOCS_ENV")
if env is None or env == "preview":
    from preview import *
