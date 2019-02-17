# pylint: disable=no-name-in-module,import-error
from JsonTableParser import JsonTableParser

class TableManager:
    """ """
    def __init__(self, configFile):
        self.url_to_table_mapping = {}
        self.configFile = configFile
        self.config = JsonTableParser.parse_json_from_file(self.configFile)
        if(self.config is None):
            raise Exception(f"TableManager::__init__() => Error: failed to load json data from {self.configFile}")

        self.load_config()

    def load_config(self):
        """ """
        return self.config
            
