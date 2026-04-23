class BettingPreferences:
    def __init__(self, *args):
        (
            self.id, self.gambler_id,
            self.min_bet, self.max_bet,
            self.preferred_game, self.auto_play,
            self.session_limit
        ) = args