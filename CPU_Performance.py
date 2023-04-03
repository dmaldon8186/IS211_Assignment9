import requests
from bs4 import BeautifulSoup

url = 'https://www.cpubenchmark.net/high_end_cpus.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('ul', {'class': 'chartlist'})
rows = table.find_all('li')

for row in rows[:20]:
    name = row.find("span", attrs = {"class":"prdname"}).text.strip()
    score = row.find("span", attrs = {"class":"count"}).text.strip()
    print(name, score)