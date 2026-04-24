class RunningTotals:
    def __init__(self):
        self.total_wins = 0
        self.total_losses = 0
        self.balance_history = []
        self.net_profit = 0

    def update(self, result):
        if result.outcome == "WIN":
            self.total_wins += result.win_amount
        else:
            self.total_losses += result.loss_amount

        self.net_profit = self.total_wins - self.total_losses
        self.balance_history.append(result.stake_after)