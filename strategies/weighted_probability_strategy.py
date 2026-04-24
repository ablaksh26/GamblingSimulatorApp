import random
from strategies.outcome_base import OutcomeStrategy

class WeightedProbabilityStrategy(OutcomeStrategy):
    def __init__(self, house_edge=0.05):
        self.house_edge = house_edge

    def determine(self, probability):
        adjusted = probability * (1 - self.house_edge)
        return "WIN" if random.random() < adjusted else "LOSS"