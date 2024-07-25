
import requests

response = requests.get("https://api.github.com/users/srikanthpragada")
if response.status_code != 200:  # Ok
    print("Sorry! Could not get details")
    exit(1)

details = response.json()

print("Name      :", details["name"])
print("Location  :", details["location"])
print("Company   :", details["company"])
