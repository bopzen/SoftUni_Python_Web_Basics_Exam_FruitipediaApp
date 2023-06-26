from django.core import validators


def validate_profile_names_start(value):
    if not value[0].isalpha():
        raise validators.ValidationError("Your name must start with a letter!")


def validate_fruit_name(value):
    for ch in value:
        if not ch.isalpha():
            raise validators.ValidationError("Fruit name should contain only letters!")
