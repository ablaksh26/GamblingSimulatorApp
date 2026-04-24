class ValidationConfig:

    def __init__(self):
        self.min_stake = 1
        self.max_stake = 1_000_000

        self.min_bet = 1
        self.max_bet = 100_000

        self.min_probability = 0.0
        self.max_probability = 1.0

        self.strict_mode = True
        self.allow_zero_stake = False