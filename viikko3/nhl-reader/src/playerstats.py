class PlayerStats():
    def __init__(self, playerreader):
        self.players = playerreader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []

        for player_obj in self.players:
            if player_obj.nationality == nationality:
                players.append(player_obj)

        sorted_players = sorted(players, key=lambda player: player.assists + player.goals, reverse=True)
        return sorted_players
