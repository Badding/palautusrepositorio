class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.assists = dict['assists']
        self.goals = dict['goals']
        self.team = dict['team']
    
    def getNationality(self):
        return self.nationality

    def get_points(self):
        return self.goals + self.assists

    def __lt__(self, other):
        return self.goals + self.assists > other.goals + other.assists

    def __str__(self):
        return f"{self.name} team {self.team}  goals {self.goals} assists {self.assists}"
