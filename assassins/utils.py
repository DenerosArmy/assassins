from random import choice, random
import time

from assassins.models import *


def add_player(uid, access_token, first_name, last_name, gender, photo, admin=False):
    lat = 37.775 + random() / 800
    lng = -122.395 + random() / 800
    new_player = Assassin.objects.get_or_create(facebook_id=uid,
                                         access_token=access_token,
                                         first_name=first_name,
                                         last_name=last_name,
                                         gender=gender,
                                         photo=photo,
                                         location_lat=lat,
                                         location_long=lng,
                                         session_id="0",
                                         alive=True,
                                         kills=0,
                                         is_admin=admin)
    hunter = random_player(new_player)
    victim = hunter.target_id
    new_player[0].target_id = victim
    hunter.target_id = uid
    new_player[0].save()
    hunter.save()
    victim = Assassin.objects.get(facebook_id=victim)
    return new_player[0], victim

def random_player(player):
    random_player = choice(Assassin.objects.filter(alive=True))
    while player is random_player:
        random_player = choice(Assassin.objects.filter(alive=True))
    return random_player

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


def post_to_feed(message, from_user=None, to_user=None, session="0"):
    now = time.time()
    Feed.objects.create(message=message,
                        from_user=from_user, 
                        to_user=to_user, 
                        session=session,
                        create_time=now)

def get_feed(session=None):
    return Feed.objects.order_by("-create_time")


def execute_kill(uid):
    killer = Assassin.objects.get(facebook_id=uid)
    killer.kills += 1
    victim = killer.target_id
    victim = Assassin.objects.get(facebook_id=victim)
    victim.alive = False
    #killer.target_id = victim.target_id
    killer.save()
    victim.save()

def execute_revive(uid):
    player = Assassin.objects.get(facebook_id=uid)
    player.alive = True
    player.save()

def execute_revive_all():
    for player in Assassin.objects.filter():
    #for player in Assassin.objects.filter(alive=False):
        lat = 37.775 + random() / 800
        lng = -122.395 + random() / 800
        player.location_lat = lat
        player.location_long = lng
        player.alive = True
        player.save()

def add_bomb(owner_id, target_id, bomb_type, bomb_lat, bomb_long, secs=None):
    Bombs.objects.create(owner_id=owner_id,
                        target_id=target_id,
                        bomb_type=bomb_type,
                        bomb_lat=bomb_lat,
                        bomb_long=bomb_long,
                        seconds_to_detonation=secs)

def get_bombs_on_me(uid):
    return Bombs.objects.filter(target_id=uid)
