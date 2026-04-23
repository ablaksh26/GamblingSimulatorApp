from strategies.base_strategy import BettingStrategy

class FibonacciStrategy(BettingStrategy):
    def __init__(self):
        self.sequence = [1, 1]

    def get_bet_amount(self, current_stake, context):
        if context.get("last_outcome") == "LOSS":
            self.sequence.append(self.sequence[-1] + self.sequence[-2])
        else:
            self.sequence = [1, 1]
        return self.sequence[-1]