import time

class GameRecord:
    def __init__(self, bet_amount, outcome, stake_before, stake_after):
        self.bet_amount = bet_amount
        self.outcome = outcome
        self.stake_before = stake_before
        self.stake_after = stake_after
        self.duration = 0

    def set_duration(self, start):
        self.duration = time.time() - start