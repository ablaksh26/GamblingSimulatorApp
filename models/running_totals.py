class RunningTotals:

    def __init__(self):
        self.total_winnings = 0
        self.total_losses = 0
        self.balance_history = []
        self.net_profit = 0

    def update(self, result):
        self.total_winnings += result.win_amount
        self.total_losses += result.loss_amount

        self.net_profit = self.total_winnings - self.total_losses
        self.balance_history.append(result.stake_after)

    def profit_factor(self):
        return self.total_winnings / self.total_losses if self.total_losses else float('inf')