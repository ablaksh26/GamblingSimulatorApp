from enum import Enum

class OddsType(Enum):
    FIXED = "FIXED"
    PROBABILITY_BASED = "PROBABILITY_BASED"
    AMERICAN = "AMERICAN"
    DECIMAL = "DECIMAL"


class OddsConfig:
    def __init__(self, odds_type: OddsType, value: float):
        self.odds_type = odds_type
        self.value = value  # meaning depends on type

    def payout(self, bet_amount, probability=None):
        if self.odds_type == OddsType.FIXED:
            return bet_amount * self.value

        if self.odds_type == OddsType.PROBABILITY_BASED:
            # inverse of probability (e.g., p=0.5 -> 2x)
            if not probability:
                raise Exception("Probability required")
            return bet_amount * (1 / probability)

        if self.odds_type == OddsType.DECIMAL:
            return bet_amount * self.value

        if self.odds_type == OddsType.AMERICAN:
            if self.value > 0:
                return bet_amount * (self.value / 100)
            else:
                return bet_amount * (100 / abs(self.value))

        raise Exception("Invalid odds type")