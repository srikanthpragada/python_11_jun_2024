from bs4 import BeautifulSoup
import requests

WEBSITE = "http://www.srikanthtechnologies.com"

resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")

links = bs.find_all("a")   # find all <a> elements
hrefs = set()

for link in links:
    href = link['href']

    if href.startswith("javascript:void"):
        continue

    if href.startswith("http"):  # absolute URL
        hrefs.add(href)
    else:
        if href.startswith("/"):   # relative URL with / at the beginning
            hrefs.add(WEBSITE + href)
        else:
            hrefs.add(WEBSITE + '/' + href)  # relative without / at the beginning

for href in sorted(hrefs):
    print(href)

print("Count = ", len(hrefs))
