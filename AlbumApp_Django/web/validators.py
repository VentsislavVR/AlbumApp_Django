from django.core import exceptions


def validate_string_alphanumeric(value):
    for ch in value:
        if not ch.isalnum() and ch != '-':
            raise exceptions.ValidationError(
                'Ensure this value contains only alphabetic characters,numbers and underscores!'
            )


