class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players() 

    def top_scorers_by_nationality(self, nationality):
        filtered_players = [p for p in self.players if p.nationality == nationality]
        filtered_player_points = [p.points for p in filtered_players]
        filtered_player_points = sorted(filtered_player_points)
    
        filtered_players_sorted = []
        seen_players = set()  
    
        while filtered_player_points:
            top_points = filtered_player_points.pop() 
    
            top_players = [p for p in filtered_players if (p.goals + p.assists) == top_points]
    
            for player in top_players:
                if player not in seen_players:
                    filtered_players_sorted.append(player)
                    seen_players.add(player)
        return filtered_players_sorted