from django.db import models


class Player(models.Model):
    facebook_id = models.CharField(primary_key=True, max_length=16)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=8)
    photo = models.CharField(max_length=128)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    session = models.ForeignKey('Session')
    is_admin = models.BooleanField()


class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=128)
    description = models.TextField()


class Feed(models.Model):
    post_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session)
    from_user = models.CharField(max_length=16)
    to_user = models.CharField(max_length=16)
    message = models.CharField(max_length=256)
    create_time = models.IntegerField()


class Assassin(Player):
    kills = models.IntegerField()
    target_id = models.CharField(max_length=16)
    games = models.ForeignKey('Session')
    alive = models.BooleanField()


class AssassinSession(Session):
    live_players = models.IntegerField()
    time = models.FloatField()
    length = models.IntegerField()


class Bombs(models.Model):
    owner_id = models.CharField(max_length=16)
    target_id = models.CharField(max_length=16)
    bomb_type = models.CharField(max_length=8)
    bomb_lat = models.FloatField()
    bomb_long = models.FloatField()
    seconds_to_detonation = models.IntegerField()
