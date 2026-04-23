class Bet:
    def __init__(self, gambler_id, amount, probability, stake_before):
        self.gambler_id = gambler_id
        self.amount = amount
        self.probability = probability
        self.stake_before = stake_before
        self.outcome = None
        self.stake_after = None

    def calculate_win_amount(self):
        return self.amount * (1 / self.probability)