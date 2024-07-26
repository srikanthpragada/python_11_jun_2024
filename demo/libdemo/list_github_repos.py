import requests

user = input("Enter github user id :")
response = requests.get(f"https://api.github.com/users/{user}/repos?per_page=10&page=1&sort=created&direction=desc")
if response.status_code != 200:  # Ok
    print("Sorry! Could not get details")
    exit(1)

repos = response.json()  # list of dict

for repo in repos:
    print(f"{repo['name']:50}  {repo['created_at'][:10]:}  {repo['updated_at'][:10]}")


