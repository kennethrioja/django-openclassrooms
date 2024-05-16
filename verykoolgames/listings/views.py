from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from listings.models import Player, Game
from listings.forms import ContactUsForm
from listings.serializers import GameSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Game.objects.all()
        serializer = GameSerializer(categories, many=True)
        return Response(serializer.data)


def index(request):
    players = Player.objects.all()
    return render(request, 'listings/index.html',
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
    # print('La méthode de requête est : ', request.method)
    # print('Les données POST sont : ', request.POST)
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via VKG Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('index')
    else:
        form = ContactUsForm()
    return render(request, 'listings/contact.html',
                  {'players': players,
                   'games': games,
                   'form': form})


def games(request):
    players = Player.objects.all()
    games = Game.objects.all()
    return render(request, 'listings/games.html',
                  {'players': players,
                   'games': games})


def games_detail(request, game_id):
    obj = get_object_or_404(Game, id=game_id)
    game = Game.objects.get(id=game_id)
    return render(request, 'listings/games_detail.html', {'game': game})
