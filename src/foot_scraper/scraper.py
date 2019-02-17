# pylint: disable=no-name-in-module,import-error
import requests
from bs4 import BeautifulSoup, SoupStrainer
from TableManager import TableManager
from config import Config


def main():
    configs = Config.getConfigs()

    for config in configs:
        page = requests.get(config["url"])
        soup = BeautifulSoup(page.text, 'html.parser')
        tables = config["tables"]
        getTableData(tables, soup)
        

def getTableData(tables, soup):
    for table in tables:
        tableDef = table["table_definition"]
        rowDef = tableDef["row_definition"]
        keyName = rowDef["key_name"]
        colDef = rowDef["column_definition"]
        playerData = colDef["player_data"]
        dataDesc = colDef["data_description"]
       
        # tableData = parseData(rootPath, soup)
        players = parseData(playerData, soup)
        # # player = players.pop(0)
        # print(players.prettify())
        for player in players:
            print(player.text)
       

def parseData(path, soup):
    cleanedData = soup.find_all(path)
    # for key,value in path:
    #     if(value is not None):
    #         cleanedData = soup.find_all(key, attrs={value})
    #     else:
    #         cleanedData = soup.find_all(key)

    return cleanedData


if __name__ == "__main__":
    main()