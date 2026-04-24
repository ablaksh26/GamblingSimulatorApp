class WinLossStatistics:

    def __init__(self):
        self.wins = 0
        self.losses = 0

        self.current_win_streak = 0
        self.current_loss_streak = 0

        self.max_win_streak = 0
        self.max_loss_streak = 0

        self.total_win_amount = 0
        self.total_loss_amount = 0

        self.largest_win = 0
        self.largest_loss = 0

    def update(self, result):

        if result.outcome == "WIN":
            self.wins += 1
            self.current_win_streak += 1
            self.current_loss_streak = 0

            self.total_win_amount += result.win_amount
            self.largest_win = max(self.largest_win, result.win_amount)

            self.max_win_streak = max(self.max_win_streak, self.current_win_streak)

        else:
            self.losses += 1
            self.current_loss_streak += 1
            self.current_win_streak = 0

            self.total_loss_amount += result.loss_amount
            self.largest_loss = max(self.largest_loss, result.loss_amount)

            self.max_loss_streak = max(self.max_loss_streak, self.current_loss_streak)

    def summary(self):
        total = self.wins + self.losses
        win_rate = (self.wins / total) * 100 if total else 0

        avg_win = self.total_win_amount / self.wins if self.wins else 0
        avg_loss = self.total_loss_amount / self.losses if self.losses else 0

        return {
            "wins": self.wins,
            "losses": self.losses,
            "win_rate": win_rate,
            "avg_win": avg_win,
            "avg_loss": avg_loss,
            "largest_win": self.largest_win,
            "largest_loss": self.largest_loss,
            "max_win_streak": self.max_win_streak,
            "max_loss_streak": self.max_loss_streak
        }