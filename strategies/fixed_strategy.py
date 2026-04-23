from strategies.base_strategy import BettingStrategy

class FixedAmountStrategy(BettingStrategy):
    def __init__(self, amount):
        self.amount = amount

    def get_bet_amount(self, current_stake, context):
        return self.amount