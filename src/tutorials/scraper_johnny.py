import requests
from bs4 import BeautifulSoup

def main():
    url = 'http://www.espn.com/soccer/team/squad/_/id/359/arsenal'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    tables = soup.find_all(class_="Table2__tbody")
    
    for table in tables:
        getTable(table)

def getTable(table):
   stats = table.find_all(class_="Table2__td")

   for stat in stats:
        print(stat.text)

if __name__ == "__main__":
    main()