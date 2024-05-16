from rest_framework.serializers import ModelSerializer
from listings.models import Game


class GameSerializer(ModelSerializer):

    class Meta:
        model = Game
        fields = ['id', 'title']