import urllib.request
from bs4 import BeautifulSoup
import json
cities = json.load('cities.json')
date = '2008/4/18' #YYYY/M/D
f = urllib.request.urlopen("https://wunderground.com/history/airport/" + airport + "/" + date +  "/DailyHistory.html?req_city=" + city + "&req_state=" + state + "&req_statename=" + country + "&reqdb.zip=00000&reqdb.magic=264&reqdb.wmo=43295")
content = f.read()
soup = BeautifulSoup(content)
res = soup.find("table", {"id": "historyTable"})
rows = res.find_all('tr')
data = []
for row in rows:
	cols = row.find_all('td')
	cols = [ele.text.strip() for ele in cols]
	data.append([ele for ele in cols if ele])
i = 0
data = data[1:]
cleaned = []
for row in data:
	if len(row)>=2:
		cleaned.append(row[:2])
for row in cleaned:
	print(row)