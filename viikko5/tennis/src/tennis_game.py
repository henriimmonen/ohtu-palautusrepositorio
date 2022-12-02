class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score = ""

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        self.score = ""
        if self.tie():
            self.calculate_tie()
        elif self.game_point():
            self.calculate_game_point()
        else:
            self.score_player(self.player1_score)
            self.score = self.score +"-"
            self.score_player(self.player2_score)
        return self.score

    def calculate_game_point(self):
        minus_result = self.player1_score - self.player2_score
        if minus_result == 1:
            self.score = "Advantage player1"
        elif minus_result == -1:
            self.score = "Advantage player2"
        elif minus_result >= 2:
            self.score = "Win for player1"
        else:
            self.score = "Win for player2"

    def tie(self):
        if self.player1_score == self.player2_score:
            return True
        return False

    def game_point(self):
        if self.player1_score >= 4 or self.player2_score >= 4:
            return True
        return False

    def score_player(self, score):
        if score == 0:
            self.score = self.score + "Love"
        elif score == 1:
            self.score = self.score + "Fifteen"
        elif score == 2:
            self.score = self.score + "Thirty"
        elif score == 3:
            self.score = self.score + "Forty"

    def calculate_tie(self):
        if self.player1_score == 0:
            self.score = "Love-All"
        elif self.player1_score == 1:
            self.score = "Fifteen-All"
        elif self.player1_score == 2:
            self.score = "Thirty-All"
        elif self.player1_score == 3:
            self.score = "Forty-All"
        else:
            self.score = "Deuce"