import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        response = requests.get(self.url)
        players_data = response.json()
        players = []
        for player_data in players_data:
            player = Player(
                name=player_data['name'],
                nationality=player_data['nationality'],
                team=player_data['team'],
                goals=player_data['goals'],
                assists=player_data['assists']
            )
            players.append(player)
        return players
