class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self._score_tied()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self._score_advantage_or_win()
        else:
            score = self._score_to_text(self.player1_score) + "-" + self._score_to_text(self.player2_score)
        return score

    def _score_to_text(self, score):
        score_text = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return score_text[score]
    
    def _score_tied(self):
        if self.player1_score >= 3:
            return "Deuce"
        return self._score_to_text(self.player1_score) + "-All"
    
    def _score_advantage_or_win(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return "Advantage player1"
        elif score_difference == -1:
            return "Advantage player2"
        elif score_difference >= 2:
            return "Win for player1"
        return "Win for player2"
