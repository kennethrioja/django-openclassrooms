from django.contrib import admin
from listings.models import Player
from listings.models import Game


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_year', 'genre')


class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'player', 'year', 'type')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Game, GameAdmin)
