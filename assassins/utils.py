from assassins.models import *


def add_player(uid, access_token, first_name, last_name, gender, photo, admin=False):
    Player.objects.create(facebook_id=uid,
                          access_token=access_token,
                          first_name=first_name,
                          last_name=last_name,
                          gender=gender,
                          photo=photo,
                          is_admin=admin)

def update_location(uid, latitude, longitude):
    Player.objects.get(facebook_id=uid).update(location_lat= latitude, location_long=longitude)

def get_location(uid):
    latitude = Player.objects.get(facebook_id=uid).get_location_latitude_display()
    longitude = Player.objects.get(facebook_id=uid).get_location_longitude_display()
    return latitude, longitude

def update_session(uid, session):
    Player.objects.get(facebook_id=uid).update(session=session)

def make_admin(uid):
    Player.objects.get(facebook_id=uid).update(is_admin=True)

def revoke_admin(uid):
    Player.objects.get(facebook_id=uid).update(is_admin=False)


def add_session(session_name, description, uid):
    player = Player.objects.get(facebook_id=uid)
    self.Session.create(session_name=session_name,
                        description=description,
                        creator=player)


def post_to_feed(message, from_user=None, to_user=None, session=None):
    now = datetime.datetime.now()
    now = time.mktime(now.timetuple())
    Feed.objects.create(message=message,
                        from_user=from_user, 
                        to_user=to_user, 
                        session=session,
                        create_time=now)

def get_feed(limit, session=None):
    return Feed.objects.order_by("-created_time")[:limit+1]


def kill(uid):
    Assassin.objects.get(facebook_id=uid).update(alive=False)

def add_bomb(owner_id, target_id, bomb_type, bomb_lat, bomb_long, secs=None):
    Bombs.objects.create(owner_id=owner_id,
                        target_id=target_id,
                        bomb_type=bomb_type,
                        bomb_lat=bomb_lat,
                        bomb_long=bomb_long,
                        seconds_to_detonation=secs)

def get_bombs_on_me(uid):
    return Bombs.objects.filter(target_id=uid)
