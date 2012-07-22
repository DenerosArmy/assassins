from girl.models import Admins, Feed, Game, Player

class Assassin(Player):
    kills = models.IntegerField()
    target = models.OneToOne(Assassin)
    games = models.ForeignKey(Game)

class AssassinSession(Game):
    live_players = models.IntegerField()
    time = models.FloatField()
    length = models.IntegerField()
