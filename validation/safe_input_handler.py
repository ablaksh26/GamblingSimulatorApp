from validation.input_validator import InputValidator
from validation.validation_config import ValidationConfig


class SafeInputHandler:

    def __init__(self):
        self.validator = InputValidator(ValidationConfig())

    def get_valid_number(self, prompt):

        while True:
            value = input(prompt)

            try:
                num = self.validator.parse_and_validate_numeric(value)
                return num

            except Exception as e:
                print(f"❌ Error: {e}")