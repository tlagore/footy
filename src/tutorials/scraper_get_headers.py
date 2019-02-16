import requests
import bs4
from bs4 import BeautifulSoup
import pprint
from dataclasses import dataclass, field

##
# This example was attempting to grab the headers from the table itself.
# this would give us the order that the data comes in, then instead 
# of having data_description (in ColumnDefinition) be simply the array of values, hardcoded
# to what the table should look like, we could have it be a dictionary of expected value to 
# proper name mapping, then when we scrape the header, we see order the data comes in.
# for example if we had a header
# -   P   G   F
# 
# and a mapping  for data_description
# { 'P' : 'player',
#   'G' : 'goals',
#   'F' : 'fouls }
#
# Then by pulling out the headers into an array [ '-', 'P', 'G', 'F']
#
# We see that column 0 has no relevance to our data, and we know to skip it.
# 
# Conversely, if at some point - P G F became G P F -, it wouldn't matter. Scraping the header
# would see the order of the data, and the mapping would tell us if we add the data or not.
#
# The reason that this failed is because there were instances the header cells were defined differently
#
# This may not prevent this approach entirely, but each header would need to have it's own definition
# Which may be required in the future anyways
# Example that failed:
# <thead>
#  <th><span><a>Header1</a></span><th>
#  <th><span>GoodHeader</span></th>
# </thead>
# 
# Stripped header comes out 
# 
##

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
                # if there is only one element in our find all, use find instead
                if(len(ret_val) == 1):
                    if root[1]:
                        ret_val = ret_val.find(root[0], root[1])
                    else:
                        ret_val = ret_val.find(root[0])
                else:
                    if root[1]:
                        ret_val = ret_val.find_all(root[0], root[1])
                    else:
                        ret_val = ret_val.find_all(root[0])


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
            retHeaders = [x.text for x in headers]
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

                            #TODO: dataDesc should also include the data type so we can take advantage of the nullable characters in celDef
                            if dataDesc[idx] is None:
                                continue
                            
                            cell = celDef.find_inner(col)
                            
                            # if this is our key, index the table as a row
                            if dataDesc[idx] == rowDef.key_name:
                                tableData[cell] = rowData
                            #else just populate the row
                            else:
                                rowData[dataDesc[idx]] = cell

            
            return tableData
        except Exception as e:
            print(f"TableDefinition::resolve() => Error when resolving table {e}")

                

def resolve_table():
    pp = pprint.PrettyPrinter(indent=2)

    #lst = ElementDefinition('a')
    #lst2 = Table('a', 'name', [Row('b', 'key', [DataCell('c', 'type', 'data_name', ['-'], 'data')])])
    #print(lst2.__dict__)
    
    celDef = DataCellDefinition([("span", None)], ['-'])
    dataDesc = {
        "POS":"position",
        "NO":"number",
        "NAME":"name",
        "AGE":"age",
        "APP":"appearances",
        "SUBIN":"substitutions" ,
        "S":"saves",
        "GC":"goals_against",
        "A":"assists",
        "FC":"fouls",
        "FA":"fouls_against",
        "YC":"yellow_cards",
        "RC":"red_cards"
    }
    colDef = ColumnDefinition([("td", None)], dataDesc, celDef)
    rowDef = RowDefinition([("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})], "name", colDef) 
    headerCelDef = DataCellDefinition([("span", None)], None)
    headDef = HeaderDefinition([("thead", None), ("tr", None)], headerCelDef)
    tableDef = TableDefinition(
        [("section",{"class": "Table2__responsiveTable Table2__table-outer-wrap --align-headers goalkeepers"}),
        ("table", {"class": "Table2__table__wrapper"})],
        "goalkeepers", rowDef, headDef
    )

    url = 'http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    data = tableDef.resolve(soup)

    print(tableDef.__dict__)
    print(rowDef.__dict__)
    print(colDef.__dict__)
    print(celDef.__dict__)

    return
    goaltenders = soup.find("section", {"class": "Table2__responsiveTable Table2__table-outer-wrap --align-headers goalkeepers"})
    table = goaltenders.find("table", {"class": "Table2__table__wrapper"})
    rows = table.find_all("tr", {"class": "Table2__tr Table2__tr--sm Table2__even"})

    data = [
        "position",
        "number",
        "name",
        "age",
        "appearances",
        "substitutions" ,
        "saves",
        "goals_against",
        "assists",
        "fouls",
        "fouls_against",
        "yellow_cards",
        "red_cards",
        None
    ] 

    cleaned = { }

    for row in rows:
        columns = row.find_all("td")
        data_row = {}

        for idx, col in enumerate(columns):
            data_name = data[idx]

            if(idx >= len(data)):
                break

            if data_name is None:
                continue
            
            data_cell = col.find("span").text

            if(data[idx] == "name"):
                cleaned[data_cell] = data_row
            else:
                data_row[data_name] = data_cell
                
    pp.pprint(cleaned)
                        
    #for row in rows:
    #    columns = rows.find_all("td")
    #    print(columns)


def main():
    resolve_table()

if __name__ == "__main__":
    main()