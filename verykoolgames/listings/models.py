from django.db import models


class Player(models.Model):
    name = models.fields.CharField(max_length=100)


class Game(models.Model):
    title = models.fields.CharField(max_length=100)
