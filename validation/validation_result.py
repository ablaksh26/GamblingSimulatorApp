class ValidationResult:

    def __init__(self):
        self.errors = []
        self.warnings = []

    def add_error(self, message):
        self.errors.append(message)

    def add_warning(self, message):
        self.warnings.append(message)

    def is_valid(self):
        return len(self.errors) == 0

    def summary(self):
        return {
            "valid": self.is_valid(),
            "errors": self.errors,
            "warnings": self.warnings
        }