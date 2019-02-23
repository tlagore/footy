# pylint: disable=no-name-in-module,import-error
import requests, json, jsbeautifier, html5lib, pandas as pd
from bs4 import BeautifulSoup
from config import Config

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
        headerLoc=int(config['header_loc'])
        tagsToRemove=config['tags_to_remove']
        soup = BeautifulSoup(page.text,'lxml')

        removeTags(soup, tagsToRemove)
        tables = soup.find_all('table')

        dfs=pd.read_html(str(tables), header=headerLoc)
        
        goaliesTable = dfs[goaliesTableLoc].to_json(orient='records')
        playersTable = dfs[playersTableLoc].to_json(orient='records')
        
        printFormatedJsonTable(goaliesTable)
        printFormatedJsonTable(playersTable)

def printFormatedJsonTable(table):
    print(jsbeautifier.beautify(table))

def removeTags(soup, tagsToRemove):
        for k,v in tagsToRemove:
                tags = soup.find_all(k, v)
                for tag in tags:
                        tag.decompose()

if __name__ == "__main__":
    main()