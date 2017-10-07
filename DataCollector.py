#curl -X GET "http://hotsapi.net/api/v1/replays?game_map=Volskaya%20Foundry&player=TommyGun%232872" -H "accept: application/json"
import requests

def callAPI():
    print ("dette er hots-data")

    url = "http://hotsapi.net/api/v1/replays?player=TommyGun%232872"
    resp = requests.get(url)

    print (resp.status_code)

    print (resp.content)

callAPI()
