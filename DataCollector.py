#http://hotsapi.net/api/v1/replays?game_type=QuickMatch&player={playerName} ? {#battleTag}
#http://hotsapi.net/api/v1/replays/{replay_id}
#saebu_no LhoeynJY saebu.no.mysql

import requests
import json

def callAPI():

#    url = "http://hotsapi.net/api/v1/replays?game_type=QuickMatch&player=TommyGun%232872"
    url = "http://hotsapi.net/api/v1/replays?start_date=2017-10-01&game_type=QuickMatch&player=TommyGun%232872"
    resp = requests.get(url)

    gameDict = resp.json()
    antGames = len(gameDict)
    print (antGames)
    data = {}
    data['games'] = []
#    f = open('TGhotsData.txt', 'w')
    for gameNr in range(0,3):
        game = gameDict[gameNr-1]
        gameId = game["id"]
        print (game["id"], gameNr)

        getGameData(gameId ,data)
    with open('tg.json', 'w') as outfile:
        json.dump(data, outfile)


def getGameData(gameId ,data):
    url = "http://hotsapi.net/api/v1/replays/"+str(gameId)

    print (url)
    resp = requests.get(url)
    gameDict = resp.json()
    players = gameDict["players"]
    gameDate = gameDict["game_date"]
    for player in players:
        if (player["battletag"] == "TommyGun#2872"):
            #playerData = (player["battletag"], player["hero"], player["winner"],
            #player["score"]["hero_damage"], player["score"]["siege_damage"],
            #player["score"]["time_spent_dead"], player["score"]["experience_contribution"],
            #gameDate)
            #f.write(str(playerData)+"\n")
            data['games'].append({
                'name' : player["battletag"],
                'hero' : player["hero"],
                'winner' : player["winner"],
                'hero_dmg' : player["score"]["hero_damage"],
                'siege_dmg' : player["score"]["siege_damage"],
                'time_dead' : player["score"]["time_spent_dead"],
                'exp_cont' : player["score"]["experience_contribution"],
                'game_date' : gameDate})

callAPI()
