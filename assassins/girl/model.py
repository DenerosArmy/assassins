from django.db import models

class Player(models.Model):
    facebook_id = models.CharField(unique=True)
    access_token = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField()
    photos = models.FileField()
    location_lat = models.DecimalField()
    location_long = models.DecimalField()

class Game(models.Model):
    game_id = models.IntegerField(unique=True)
    game_name = models.CharField()

class Admins(models.Model):
    facebook_id = models.ForeignKey(Player)

class Feed(models.Model):
    post_id = models.IntegerField(unique=True)
    from_user = models.ForeignKey(Player)
    to_user = models.ForeignKey(Player)
    post = models.CharField()
    create_time = models.IntegerField()
