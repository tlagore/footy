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
        tables = config["tables"]
        getTableData(tables, page)
        

def getTableData(tables, page):
    for table in tables:
        # soup = BeautifulSoup(page.text, 'html.parser')
        tableDef = table["table_definition"]
        rowDef = tableDef["row_definition"]
        colDef = rowDef["column_definition"]
        playerData = colDef["player_data"]
        dataDesc = colDef["data_description"]
        playerDetails = colDef["player_details"]
        specificTable = colDef["specific_table"]
        for k, v in specificTable:
            for key,value in v.items():
                soup = BeautifulSoup(page.text, 'html.parser', parse_only=SoupStrainer(k, {key : re.compile(value)}))
        # players = parseData(playerData, soup)
        for key, value in playerDetails:
            playersNames = parseRegexStar(key, value, soup)

        
        # Get Players stats here
        # for key, value in playerData:
        #     playerStats = parseRegexIgnore(key,value,soup)

        # for stat in playerStats:
        #     print(stat.text)

        for playerName in playersNames:
            rowDef.update({playerName.text:""})

        for key, value in rowDef.items():
            print(key,"=>", value)
       

def parseRegexStar(key, value, soup):
    for k,v in value.items():
        cleanedData = soup.find_all(key, {k : re.compile(v+"*")})

    return cleanedData

def parseRegexIgnore(key, value, soup):
    cleanedData = soup.find_all(key, re.compile(value))

    return cleanedData

if __name__ == "__main__":
    main()