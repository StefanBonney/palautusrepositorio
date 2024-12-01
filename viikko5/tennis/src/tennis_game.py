class TennisGame:

    # map numeric scores to tennis point names
    POINT_SCORES = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    def __init__(self, player1_name: str, player2_name: str):
        """ Initialize the TennisGame with players and scores 
        """
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name: str) -> None:
        """ Increment score for player winning point 
        """
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self) -> str:
        """ Main scoring logic that determines which scoring method to use.
            Returns:
                SAME SCORE
                - "Love-All" if both players have 0 points
                - "Fifteen-All" if both players have 1 point
                - "Thirty-All" if both players have 2 points
                - "Deuce" if both players have 3 or more points
                HIGH SCORE
                - "Advantage player1" (4-3)
                - "Advantage player2" (3-4)
                - "Win for player1" (5-3, 6-4, or more)
                - "Win for player2" (3-5, 4-6, or more)
                REGULAR SCORE
                - "Love-Fifteen" (0-1)
                - "Thirty-Fifteen" (2-1)
                - "Forty-Thirty" (3-2)
                - "Fifteen-Thirty" (1-2)
                - "Thirty-Forty" (2-3)
        """
        # Case 1: Both players have the same score
        if self.player1_score == self.player2_score:
            return self._get_equal_score()
        # Case 2: At least one player has a score of 4 or more, indicating advantage or win
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._get_advantage_or_win_score()
        # Case 3: Regular score display when scores are not tied or in advantage/win state
        else:
            return self._get_regular_score()

    def _get_equal_score(self) -> str:
        """ score string for a tied game
        """
        if self.player1_score <= 2:
            # For scores up to 30-all, use the format "Score-All"
            return self.POINT_SCORES[self.player1_score] + "-All"
        # Scores of 40-40 and above are "Deuce"
        return "Deuce"

    def _get_advantage_or_win_score(self) -> str:
        """ score string when one player has an advantage or has won
        """
        # Calculate the difference in scores to determine advantage/win
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _get_regular_score(self) -> str:
        """ score string for a regular game state - not tied, advantage, or win
        """
        temp_player1_score = self.POINT_SCORES[self.player1_score]
        temp_player2_score = self.POINT_SCORES[self.player2_score]
        return f"{temp_player1_score}-{temp_player2_score}" # f.ex. "Love-Fifteen" (0-1)
