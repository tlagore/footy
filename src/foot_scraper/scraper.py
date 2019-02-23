# pylint: disable=no-name-in-module,import-error
import requests
import pandas as pd
import html5lib
from bs4 import BeautifulSoup
from config import Config
import json
import jsbeautifier

def main():
    configs = Config.getConfigs()
    for config in configs:
        urls = config["urls"]
        for url in urls:
            page = requests.get(url)
            getTableData(page, config)
        

def getTableData(page, config):
        goaliesTableLoc=int(config['goalie_table_loc'])
        playersTableLoc=int(config['player_table_loc'])
        soup = BeautifulSoup(page.text,'lxml')
        tables = soup.find_all('table')

        dfs=pd.read_html(str(tables), header=0)
        
        goaliesTable = dfs[goaliesTableLoc].to_json(orient='records')
        playersTable = dfs[playersTableLoc].to_json(orient='records')
        
        printFormatedJsonTable(goaliesTable)
        printFormatedJsonTable(playersTable)

def printFormatedJsonTable(table):
    print(jsbeautifier.beautify(table))

if __name__ == "__main__":
    main()