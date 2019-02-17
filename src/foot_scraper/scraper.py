# pylint: disable=no-name-in-module,import-error
import requests
from bs4 import BeautifulSoup, SoupStrainer
from TableManager import TableManager
from config import Config
import re


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
        playerDetails = colDef["player_details"]
       
        # players = parseData(playerData, soup)
        for key, value in playerDetails:
            playersNames = parsePlayerNames(key, value, soup)

        # Get Players stats here
        playerStats = soup.find_all(playerData)

        for player in playersNames:
            rowDef.update({player.text:""})

        for key, value in rowDef.items():
            print(key,"=>", value)
       

def parsePlayerNames(key, value, soup):

    for k,v in value.items():
        cleanedData = soup.find_all(key, {k : re.compile(v)})

    return cleanedData


if __name__ == "__main__":
    main()