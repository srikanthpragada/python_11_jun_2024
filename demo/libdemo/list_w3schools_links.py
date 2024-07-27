from bs4 import BeautifulSoup
import requests

WEBSITE = "https://www.w3schools.com"

resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")
hrefs = set()

for link in links:
    href = link['href']

    if href.startswith("javascript:void"):
        continue

    if href.startswith("http"):
        hrefs.add(href)
    else:
        if href.startswith("/"):
            hrefs.add(WEBSITE + href)
        else:
            hrefs.add(WEBSITE + '/' + href)

for href in sorted(hrefs):
    print(href)

print("Count = ", len(hrefs))
