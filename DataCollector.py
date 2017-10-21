#http://hotsapi.net/api/v1/replays?game_type=QuickMatch&player={playerName} ? {#battleTag}
#http://hotsapi.net/api/v1/replays/{replay_id}

import requests
import json

def callAPI():

#    url = "http://hotsapi.net/api/v1/replays?game_type=QuickMatch&player=TommyGun%232872"
    url = "http://hotsapi.net/api/v1/replays?start_date=2017-10-01&game_type=QuickMatch&player=TommyGun%232872"
    resp = requests.get(url)

    gameDict = resp.json()
    antGames = len(gameDict)
    print (antGames)

    for gameNr in range(0,antGames):
        game = gameDict[gameNr-1]
        gameId = game["id"]
        print (game["id"], gameNr)

        getGameData(gameId)

'''
    url_game_id = "http://hotsapi.net/api/v1/replays/"+"gameId"

    game_resp = requests.get(url_game_id)

    print (game_resp.json().players[0])
'''
def getGameData(gameId):
    url = "http://hotsapi.net/api/v1/replays/"+str(gameId)
    print (url)
    resp = requests.get(url)
    gameDict = resp.json()
    players = gameDict["players"]
    for player in players:
        if (player["battletag"] == "TommyGun#2872"):
            print (player["battletag"], player["hero"], player["winner"],
            player["score"]["hero_damage"], player["score"]["siege_damage"],
            player["score"]["time_spent_dead"], player["score"]["experience_contribution"])

callAPI()
