class Player:
    def __init__(self, p_dict):
        self.name = p_dict.get("name")
        self.team = p_dict.get("team")
        self.goals = p_dict.get("goals")
        self.assists = p_dict.get("assists")
        self.nationality = p_dict.get("nationality")
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:<20} {self.team}  {self.goals} + {self.assists} = {self.points}"
