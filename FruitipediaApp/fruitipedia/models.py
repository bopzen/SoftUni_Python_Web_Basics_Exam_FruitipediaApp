from django.db import models
from django.core import validators
from FruitipediaApp.fruitipedia.validators import validate_profile_names_start, validate_fruit_name


class Profile(models.Model):
    MIN_FIRST_NAME_LENGTH = 2
    MAX_FIRST_NAME_LENGTH = 25
    MIN_LAST_NAME_LENGTH = 1
    MAX_LAST_NAME_LENGTH = 35
    MAX_EMAIL_LENGTH = 40
    MIN_PASSWORD_LENGTH = 8
    MAX_PASSWORD_LENGTH = 20
    DEFAULT_AGE = 18

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_FIRST_NAME_LENGTH),
            validate_profile_names_start,
        ),
        null=False,
        blank=False
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_LAST_NAME_LENGTH),
            validate_profile_names_start,
        ),
        null=False,
        blank=False
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LENGTH,
        null=False,
        blank=False
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_PASSWORD_LENGTH),
        ),
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=True,
        blank=True
    )

    age = models.PositiveIntegerField(
        default=DEFAULT_AGE,
        null=False,
        blank=True
    )


class Fruit(models.Model):
    MIN_NAME_LENGTH = 2
    MAX_NAME_LENGTH = 30

    name = models.CharField(
        max_length=MAX_NAME_LENGTH,
        validators=(
            validators.MinLengthValidator(MIN_NAME_LENGTH),
            validate_fruit_name,
        ),
        null=False,
        blank=False
    )

    image_url = models.URLField(
        null=False,
        blank=False
    )

    description = models.TextField(
        null=False,
        blank=False
    )

    nutrition = models.TextField(
        null=True,
        blank=True
    )
