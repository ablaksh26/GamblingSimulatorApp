class WinLossStatistics:

    def __init__(self):
        self.wins = 0
        self.losses = 0

        self.current_win_streak = 0
        self.current_loss_streak = 0

        self.max_win_streak = 0
        self.max_loss_streak = 0

    def update(self, result):
        if result.outcome == "WIN":
            self.wins += 1
            self.current_win_streak += 1
            self.current_loss_streak = 0
            self.max_win_streak = max(self.max_win_streak, self.current_win_streak)
        else:
            self.losses += 1
            self.current_loss_streak += 1
            self.current_win_streak = 0
            self.max_loss_streak = max(self.max_loss_streak, self.current_loss_streak)

    def summary(self):
        total = self.wins + self.losses
        win_rate = (self.wins / total) * 100 if total else 0

        return {
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": win_rate,
            "max_win_streak": self.max_win_streak,
            "max_loss_streak": self.max_loss_streak
        }