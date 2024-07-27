from bs4 import BeautifulSoup
import requests

WEB_PAGE = "https://www.tiobe.com/tiobe-index"

resp = requests.get(WEB_PAGE)
bs = BeautifulSoup(resp.text, "html.parser")

table = bs.find(id="top20")
#print(table.tbody)
rows = table.tbody.find_all("tr")

for row in rows[:10]:
    cols = row.find_all("td")
    print(f"{cols[4].text:15}   {cols[5].text}")


