import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for p_dict in response:
        player = Player(p_dict)
        players.append(player)

    #print("Oliot:")

    #for player in players:
        #print(player)

    finnish_players = [p for p in players if p.nationality == "FIN"]
    #for player in finnish_players:
        #print(player)
    finnish_player_points = [p.points for p in finnish_players]
    finnish_player_points = sorted(finnish_player_points)
    #print(finnish_player_points)

    #---------------------------------------------------------------------------
    finnish_players_sorted = []
    seen_players = set()  

    while finnish_player_points:
        top_points = finnish_player_points.pop() 

        top_players = [p for p in finnish_players if (p.goals + p.assists) == top_points]

        for player in top_players:
            if player not in seen_players:
                finnish_players_sorted.append(player)
                seen_players.add(player)
    #---------------------------------------------------------------------------

    print("Players from FIN\n")
    for player in finnish_players_sorted:
        print(player)


main()