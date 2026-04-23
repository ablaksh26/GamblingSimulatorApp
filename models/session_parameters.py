class SessionParameters:
    def __init__(self, min_stake, max_stake, min_bet, max_bet, max_games, max_duration, probability):
        self.min_stake = min_stake
        self.max_stake = max_stake
        self.min_bet = min_bet
        self.max_bet = max_bet
        self.max_games = max_games
        self.max_duration = max_duration
        self.probability = probability