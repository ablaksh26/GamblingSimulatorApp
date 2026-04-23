import datetime

class BettingSession:
    def __init__(self):
        self.bets = []
        self.start_time = datetime.datetime.now()
        self.end_time = None

    def add_bet(self, bet):
        self.bets.append(bet)

    def close(self):
        self.end_time = datetime.datetime.now()

    def summary(self):
        wins = sum(1 for b in self.bets if b.outcome == "WIN")
        losses = sum(1 for b in self.bets if b.outcome == "LOSS")
        return {
            "total_bets": len(self.bets),
            "wins": wins,
            "losses": losses
        }