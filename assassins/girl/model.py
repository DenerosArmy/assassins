from django.db import models

class Player(models.Model):
    facebook_id = models.CharField(primary_key=True)
    access_token = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()
    gender = models.CharField()
    photo = models.CharField()
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

    def update_location(self, uid, loc_lat, loc_long):
        self.objects.get(facebook_id=uid).update(location_lat= loc_lat, location_long=loc_long)

    def update_session(self, uid, session):
        self.objects.get(facebook_id=uid).update(session=session)

    def make_admin(self, uid):
        self.objects.get(facebook_id=uid).update(is_admin=True)

    def revoke_admin(self, uid):
        self.objects.get(facebook_id=uid).update(is_admin=False)

class Session(models.Model):
    session_id = models.AutoField(primary_key=True)
    session_name = models.CharField()

    def add_session(self, session_name=None):
        self.objects.create(session_name=session_name)

class Feed(models.Model):
    post_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(Session)
    from_user = models.ForeignKey(Player)
    to_user = models.ForeignKey(Player)
    message = models.CharField()
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
        return self.objects.all()[]