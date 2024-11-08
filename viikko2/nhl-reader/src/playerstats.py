class PlayerStats:
    def __init__(self, reader):
        self.players = reader.getPlayers()
        self.nationalities = list(set(player.getNationality() for player in self.players))

    def getPlayersByNationality(self, nationality):
        return list(filter(lambda x: x.getNationality() == nationality, self.players))
    
    def top_scorers_by_nationality(self, nationality):
        players = self.getPlayersByNationality(nationality)
        return sorted(players)

    def get_nationalities(self):
        return self.nationalities
