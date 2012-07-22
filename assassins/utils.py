import time

from assassins.models import *


def add_player(uid, access_token, first_name, last_name, gender, photo, admin=False):
    Assassin.objects.create(facebook_id=uid,
                            access_token=access_token,
                            first_name=first_name,
                            last_name=last_name,
                            gender=gender,
                            photo=photo,
                            location_lat=0.0,
                            location_long=0.0,
                            session_id="0",
                            alive=True,
                            kills=0,
                            is_admin=admin)

def add_target(uid, target_id):
    player = Assassin.objects.get(facebook_id=uid)
    player.target_id = target_id
    player.save()

def update_location(uid, latitude, longitude):
    player = Player.objects.get(facebook_id=uid)
    player.location_lat = latitude
    player.location_long = longitude
    player.save()

def get_location(uid):
    latitude = Player.objects.get(facebook_id=uid).location_lat
    longitude = Player.objects.get(facebook_id=uid).location_long
    return latitude, longitude

def update_session(uid, session):
    player = Player.objects.get(facebook_id=uid)
    player.session = session
    player.save()

def make_admin(uid):
    Player.objects.get(facebook_id=uid).update(is_admin=True)

def revoke_admin(uid):
    Player.objects.get(facebook_id=uid).update(is_admin=False)


def add_session(session_name, description, uid):
    player = Player.objects.get(facebook_id=uid)
    Session.create(session_name=session_name,
                   description=description)


def post_to_feed(message, from_user=None, to_user=None, session=None):
    now = time.time()
    Feed.objects.create(message=message,
                        from_user=from_user, 
                        to_user=to_user, 
                        session=session,
                        create_time=now)

def get_feed(limit, session=None):
    return Feed.objects.order_by("-created_time")[:limit+1]


def kill(uid):
    victim = Assassin.objects.get(facebook_id=uid)
    victim.alive = False
    victim.save()

def add_bomb(owner_id, target_id, bomb_type, bomb_lat, bomb_long, secs=None):
    Bombs.objects.create(owner_id=owner_id,
                        target_id=target_id,
                        bomb_type=bomb_type,
                        bomb_lat=bomb_lat,
                        bomb_long=bomb_long,
                        seconds_to_detonation=secs)

def get_bombs_on_me(uid):
    return Bombs.objects.filter(target_id=uid)
