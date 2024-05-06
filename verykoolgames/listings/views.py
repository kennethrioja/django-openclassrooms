from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Player
from listings.models import Game


def hello(request):
    players = Player.objects.all()
    return render(request, 'listings/hello.html',
                  {'players': players})


def about(request):
    players = Player.objects.all()
    games = Game.objects.all()
    return render(request, 'listings/about.html',
                  {'players': players,
                   'games': games})


def contact(request):
    players = Player.objects.all()
    games = Game.objects.all()
    return render(request, 'listings/contact.html',
                  {'players': players,
                   'games': games})


def games(request):
    players = Player.objects.all()
    games = Game.objects.all()
    return render(request, 'listings/games.html',
                  {'players': players,
                   'games': games})
