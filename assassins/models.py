from django.db import models

from girl.models import Feed, Player, Session


class Assassin(Player):
    kills = models.IntegerField()
    target_id = models.CharField()
    games = models.ForeignKey(Session)

class AssassinSession(Session):
    live_players = models.IntegerField()
    time = models.FloatField()
    length = models.IntegerField()
