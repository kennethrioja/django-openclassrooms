from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Player(models.Model):

    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    birth_year = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Game(models.Model):

    class Type(models.TextChoices):
        ADVENTURE = 'AD'
        SPORT = 'SP'
        PUZZLE = 'PU'

    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        validators=[MinValueValidator(2023), MaxValueValidator(2024)]
    )
    type = models.fields.CharField(choices=Type.choices, max_length=5)
    player = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'
