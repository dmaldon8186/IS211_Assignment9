import requests
from bs4 import BeautifulSoup

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('tbody')
rows = table.find_all('tr')

for row in rows[:20]:
    cells = row.find_all('td')
    if len(cells) > 1:
        name = cells[0].find('a').text.strip()
        team = cells[0].find("span", attrs = {"class":"CellPlayerName-team"}).text.strip()
        touchdowns = cells[8].text.strip()
        print(name, team, touchdowns)