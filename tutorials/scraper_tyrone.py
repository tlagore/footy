import requests
import bs4
from bs4 import BeautifulSoup
import pprint
from dataclasses import dataclass, field
import json
import os

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

class TableManager:
    """ """
    def __init__(self, configFile):
        self.url_to_table_mapping = {}
        self.configFile = configFile
        self.config = JsonTableParser.parse_json_from_file(self.configFile)
        if(self.config is None):
            raise Exception(f"TableManager::__init__() => Error: failed to load json data from {self.configFile}")

        self.load_tables()

    def load_tables(self):
        """ """
        for conf in self.config:
            url = conf["url"]

class ElementDefinition:
    """ 
        ElementDefinition defines an html element and how to find it in some set of html

        root path will be of form [('elementType', { 'html_tag': 'value'})]
        this describes the path to find an element. For example:
        <html>
            <div class="some">
                <span class="data">important</span>
            </div>
            <div class="someMore">
                <span class="data">unimportant</span>
            <div>
        </html>

        To get our 'important' data, root_path would be 
            [('div', {'class': 'some'}), ('span', {'class':'data'})]
        
        The root_path should be the minimum number of tags required to uniquely identify this Element.
        """
    def __init__(self, root_path):
        self.root_path = root_path

    def find_inner(self, data):
        el = self.find(data)

        if el:
            return el.text
        
        return None

    def find(self, data):
        """ """
        try:
            ret_val = data
            for root in self.root_path:
                if root[1]:
                    ret_val = ret_val.find(root[0], root[1])
                else:
                    ret_val = ret_val.find(root[0])

            return ret_val
        except Exception as e:
            print(f"ElementDefinition::find() => exception when retrieving data {e}")
        
        return None
    
    def find_all(self, data):
        """ """
        try:
            ret_val = data
            for root in self.root_path:
                if isinstance(ret_val, bs4.element.Tag):
                    if root[1]:
                        ret_val = ret_val.find_all(root[0], root[1])
                    else:
                        ret_val = ret_val.find_all(root[0])
                elif isinstance(ret_val, bs4.element.ResultSet):
                    resSet = bs4.element.ResultSet(ret_val.source)
                    for res in ret_val:
                        if root[1]:
                            resSet += res.find_all(root[0], root[1])
                        else:
                            resSet += res.find_all(root[0])
                    
                    ret_val = resSet

            return ret_val
        except Exception as e:
            print(f"ElementDefinition::find() => exception when retrieving data {e}")

        return None

class DataDefinition:
    def __init__(self, data_type, data_name):
        self.data_type = data_type
        self.data_name = data_name

class DataCellDefinition(ElementDefinition):
    def __init__(self, root_path, null_characters):
        ElementDefinition.__init__(self, root_path)
        self.null_characters = null_characters

class ColumnDefinition(ElementDefinition):
    def __init__(self, root_path, data_descriptions, data_definition):
        ElementDefinition.__init__(self, root_path)
        self.data_descriptions = data_descriptions
        self.data_definition = data_definition

class HeaderDefinition(ElementDefinition):
    def __init__(self, root_path, header_cell_definition):
        ElementDefinition.__init__(self, root_path)
        self.header_cell_definition = header_cell_definition

class RowDefinition(ElementDefinition):
    def __init__(self, root_path, key_name, column_definition):
        ElementDefinition.__init__(self, root_path)
        self.key_name = key_name
        self.column_definition = column_definition

class TableDefinition(ElementDefinition):
    """ """
    def __init__(self, root_path, table_name, row_definition, header_definition):
        ElementDefinition.__init__(self, root_path)
        self.row_definition = row_definition
        self.header_definition = header_definition

    def get_headers(self, data):
        celDef = self.header_definition.header_cell_definition

        try:
            header = self.header_definition.find_all(data)
            headers = celDef.find_all(header)
            retHeaders = [x.text.upper() for x in headers]
            return retHeaders
        except Exception as e:
            print("error")

        return None

    def resolve(self, data):
        try:
            rowDef = self.row_definition
            colDef = rowDef.column_definition
            celDef = colDef.data_definition
            dataDesc = colDef.data_descriptions

            tableData = {}
            rowData = {}

            table = self.find(data)

            headers = self.get_headers(table)

            if(table):
                rows = rowDef.find_all(table)
                if(rows):
                    for row in rows:
                        cols = colDef.find_all(row)
                        for idx, col in enumerate(cols):
                            if idx >= len(headers):
                                break
                            #TODO: dataDesc should also include the data type so we can take advantage of the nullable characters in celDef
                            if headers[idx] is None or headers[idx] == '':
                                continue
                            
                            cell = celDef.find_inner(col)
                            key = dataDesc[headers[idx]]
                            
                            # if this is our key, index the table as a row
                            if key == rowDef.key_name:
                                tableData[cell] = rowData
                            #else just populate the row
                            else:
                                rowData[key] = cell

            
            return tableData
        except Exception as e:
            print(f"TableDefinition::resolve() => Error when resolving table {e}")

                

#def resolve_table():
#    celDef = DataCellDefinition([("span", None)], ['-'])
#    dataDesc = {
#        "POS":"position",
#        "NO":"number",
#        "NAME":"name",
#        "AGE":"age",
#        "APP":"appearances",
#        "SUBIN":"substitutions" ,
#        "S":"saves",
#        "GC":"goals_against",
#        "A":"assists",
#        "FC":"fouls",
#        "FA":"fouls_against",
#        "YC":"yellow_cards",
#        "RC":"red_cards"
#    }
#    colDef = ColumnDefinition([("td", None)], dataDesc, celDef)
#    rowDef = RowDefinition([("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})], "name", colDef) 
#    headerCelDef = DataCellDefinition([("span", None),("a", None)], None)
#    headDef = HeaderDefinition([("thead", None), ("tr", None)], headerCelDef)
#    tableDef = TableDefinition(
#        [("section",{"class": "Table2__responsiveTable Table2__table-outer-wrap --align-headers goalkeepers"}),
#        ("table", {"class": "Table2__table__wrapper"})],
#        "goalkeepers", rowDef, headDef
#    )
#
#    url = 'http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1'
#    page = requests.get(url)
#    soup = BeautifulSoup(page.text, 'html.parser')
#
#    data = tableDef.resolve(soup)


def main():
    pp = pprint.PrettyPrinter(indent=1)

    manager = TableManager("config.json")
    
    pp.pprint(manager.config)
    return
    resolve_table()

if __name__ == "__main__":
    main()