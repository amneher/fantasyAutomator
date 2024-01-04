# Special characters that are not allowed in database schemas' string fields
import typing


DISALLOWED_SPECIAL_CHARACTERS = r"<>"


# Maximum length of database schemas' string fields by default
DEFAULT_MAX_STRING_FIELD_LENGTH = 100


class ValidationException(Exception):
    def __init__(self, message: str, *args: object) -> None:
        super().__init__(*args)
        self.message = message

    def __str__(self) -> str:
        return self.message


def remove_invalid_characters(s):
    """
    Return the given string with illegal characters removed
    """
    # if set(s).intersection(DISALLOWED_SPECIAL_CHARACTERS):
    #     _logger.info(f"Disallowed characters removed from string field value '{s}'")

    return "".join(c for c in s if c not in DISALLOWED_SPECIAL_CHARACTERS)


def truncate_long_string(s, max_length):
    # if len(s) > max_length:
    #     _logger.info(f"String field value '{s}' truncated")
    return s[:max_length]


ValidationFunctions = typing.Optional[typing.List[typing.Callable[[str], str]]]


def validate_string(
    value, max_length=DEFAULT_MAX_STRING_FIELD_LENGTH, extra_validators=None
):
    if value is None:
        return None

    value = remove_invalid_characters(str(value))
    if max_length is not None:
        value = truncate_long_string(value, max_length)

    if extra_validators:
        for v in extra_validators:
            value = v(value)

    return value


def null_sanitizer(value):
    return value
