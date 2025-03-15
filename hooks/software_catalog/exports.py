import json
from pathlib import Path

import humps

from .catalog import Catalog


class JSONExport:
    def __init__(self, catalog: Catalog, props):
        self.__catalog = catalog
        self.__props = props

    @property
    def content(self):
        data = self.__catalog.export(self.__props)
        return json.dumps(humps.camelize(data))
