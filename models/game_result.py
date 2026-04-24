class GameResult:
    def __init__(self, bet_amount, outcome, stake_before, odds_config, probability):
        self.bet_amount = bet_amount
        self.outcome = outcome
        self.stake_before = stake_before

        if outcome == "WIN":
            self.win_amount = odds_config.payout(bet_amount, probability)
            self.loss_amount = 0
        else:
            self.win_amount = 0
            self.loss_amount = bet_amount

        self.stake_after = stake_before + self.win_amount - self.loss_amount

    def to_dict(self):
        return {
            "bet": self.bet_amount,
            "outcome": self.outcome,
            "win": self.win_amount,
            "loss": self.loss_amount,
            "before": self.stake_before,
            "after": self.stake_after
        }