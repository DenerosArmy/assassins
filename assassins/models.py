from django.db import models

class Player(models.Model):
    facebook_id = models.CharField(primary_key=True, max_length=16)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    gender = models.CharField(max_length=8)
    photo = models.CharField(max_length=128)
    location_lat = models.FloatField()
    location_long = models.FloatField()
    session = models.ForeignKey(Session)
    is_admin = models.BooleanField()

    def add_player(self, uid, access_token, first_name, last_name, gender, photo, admin=False):
        self.objects.create(facebook_id=uid,
                            access_token=access_token,
                            first_name=first_name,
                            last_name=last_name,
                            gender=gender,
                            photo=photo,
                            is_admin=admin)

    def update_location(self, uid, latitude, longitude):
        self.objects.get(facebook_id=uid).update(location_lat= latitude, location_long=longitude)

    def get_location(self, uid):
        latitude = self.objects.get(facebook_id=uid).get_location_latitude_display()
        longitude = self.objects.get(facebook_id=uid).get_location_longitude_display()
        return latitude, longitude

    def update_session(self, uid, session):
        self.objects.get(facebook_id=uid).update(session=session)

    def make_admin(self, uid):
        self.objects.get(facebook_id=uid).update(is_admin=True)

    def revoke_admin(self, uid):
        self.objects.get(facebook_id=uid).update(is_admin=False)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField(max_length=128)
    description = models.TextField()

    def add_session(self, session_name, description, uid):
        player = Player.objects.get(facebook_id=uid)
        self.objects.create(session_name=session_name,
                            description=description,
                            creator=player)

class Feed(models.Model):
    post_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session)
    from_user = models.ForeignKey(Player)
    to_user = models.ForeignKey(Player)
    message = models.CharField(max_length=256)
    create_time = models.IntegerField()

    def post(self, message, from_user=None, to_user=None, session=None):
        now = datetime.datetime.now()
        now = time.mktime(now.timetuple())
        self.objects.create(message=message,
                            from_user=from_user, 
                            to_user=to_user, 
                            session=session,
                            create_time=now)

    def get_feed(self, limit, session=None):
        return self.objects.order_by("-created_time")[:limit+1]

class Assassin(Player):
    kills = models.IntegerField()
    target_id = models.CharField(max_length=16)
    games = models.ForeignKey(Session)

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

    def add_bomb(self, owner_id, target_id, bomb_type, bomb_lat, bomb_long, secs=None):
        self.objects.create(owner_id=owner_id,
                            target_id=target_id,
                            bomb_type=bomb_type,
                            bomb_lat=bomb_lat,
                            bomb_long=bomb_long,
                            seconds_to_detonation=secs)

    def get_bombs_on_me(self, uid):
        return self.objects.filter(target_id=uid)

