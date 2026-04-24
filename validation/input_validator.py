import math
from validation.validation_result import ValidationResult
from validation.exceptions import *


class InputValidator:

    def __init__(self, config):
        self.config = config

    # 1. INITIAL STAKE
    def validate_initial_stake(self, stake):
        result = ValidationResult()

        if stake is None:
            result.add_error("Stake cannot be null")

        elif not isinstance(stake, (int, float)):
            result.add_error("Stake must be numeric")

        elif math.isnan(stake) or math.isinf(stake):
            result.add_error("Stake cannot be NaN or Infinity")

        elif stake < 0:
            result.add_error("Stake cannot be negative")

        elif stake < self.config.min_stake:
            result.add_error(f"Stake below minimum {self.config.min_stake}")

        elif stake > self.config.max_stake:
            result.add_error(f"Stake above maximum {self.config.max_stake}")

        return result

    # 2. BET VALIDATION
    def validate_bet_amount(self, bet, current_stake):
        result = ValidationResult()

        if bet > current_stake:
            result.add_error("Bet exceeds current stake")

        if bet < self.config.min_bet:
            result.add_error("Bet below minimum limit")

        if bet > self.config.max_bet:
            result.add_error("Bet exceeds max limit")

        return result

    # 3. LIMIT VALIDATION
    def validate_limits(self, lower, upper, initial_stake):
        result = ValidationResult()

        if lower < 0 or upper < 0:
            result.add_error("Limits cannot be negative")

        if upper <= lower:
            result.add_error("Upper limit must be greater than lower")

        if not (lower <= initial_stake <= upper):
            result.add_error("Initial stake must be within limits")

        return result

    # 4. NUMERIC PARSING
    def parse_and_validate_numeric(self, value):
        try:
            num = float(value)

            if math.isnan(num) or math.isinf(num):
                raise ValueError("Invalid number")

            return num

        except:
            raise ValidationException("Invalid numeric input", value=value)

    # 5. NON-NEGATIVE STAKE
    def validate_non_negative(self, stake):
        if stake < 0:
            raise StakeValidationException("Negative stake not allowed", value=stake)

    # 6. PROBABILITY
    def validate_probability(self, probability):
        result = ValidationResult()

        if probability < self.config.min_probability or probability > self.config.max_probability:
            result.add_error("Probability must be between 0 and 1")

        return result