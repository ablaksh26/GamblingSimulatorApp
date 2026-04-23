class StakeBoundary:

    def __init__(self, min_stake, max_stake):
        self.min_stake = min_stake
        self.max_stake = max_stake

    def validate(self, stake):
        if stake < self.min_stake:
            return "LOW"
        if stake > self.max_stake:
            return "HIGH"
        return "OK"

    def warning(self, stake):
        if stake <= self.min_stake * 1.2:
            return "⚠️ Approaching lower limit"
        if stake >= self.max_stake * 0.8:
            return "⚠️ Approaching upper limit"
        return None