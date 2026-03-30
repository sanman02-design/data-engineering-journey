import requests
import json

def fetch_football_standings():
    url= "https://api.football-data.org/v4/competitions/PL/standings"
    headers = {"X-Auth-Token": "adb6778189ef4632b73513429e5102cb"}

    response = requests.get(url, headers=headers)
    print("Status code:", response.status_code)

    data=response.json()
    
    with open("standings.json","w") as f:
        json.dump(data,f,indent=2)
    
    print("data saved to standings.json")
    print("Current matchday:", data["season"]["currentMatchday"])
    print("Top team:", data["standings"][0]["table"][0]["team"]["name"])
fetch_football_standings()
