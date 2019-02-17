import os
import json

class JsonTableParser:
    """ """
    @staticmethod
    def parse_json_from_file(file):
        #if an absolute filepath was not given, assume it is relative to this location
        if(not os.path.isabs(file)):
            file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        try:
            with open(file) as configJson:
                data = json.load(configJson)

            return data        
        except Exception as ex:
            print("error")
            print(ex)