class ValidationException(Exception):
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value


class StakeValidationException(ValidationException):
    pass


class BetValidationException(ValidationException):
    pass


class LimitValidationException(ValidationException):
    pass


class ProbabilityValidationException(ValidationException):
    pass