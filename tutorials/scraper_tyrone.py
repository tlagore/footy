import requests
from bs4 import BeautifulSoup
import pprint
from dataclasses import dataclass, field

@dataclass
class ElementDefinition:
    root_path: int
    poo: str


class TableDefinition:
    def __init__(self,url, data, ):
        """ """

def resolve_table():
    lst = ElementDefinition([1,2],1)
    print(lst.root_path)
    print(lst.poo)

    return
    pp = pprint.PrettyPrinter(indent=2)
    url = 'http://www.espn.com/soccer/team/squad/_/id/359/league/ENG.1'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
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

    len(data)

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