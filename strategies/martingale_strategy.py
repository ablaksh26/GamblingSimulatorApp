from strategies.base_strategy import BettingStrategy

class MartingaleStrategy(BettingStrategy):
    def __init__(self, base):
        self.base = base

    def get_bet_amount(self, current_stake, context):
        if context.get("last_outcome") == "LOSS":
            return context.get("last_bet", self.base) * 2
        return self.base