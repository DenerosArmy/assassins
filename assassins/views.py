import simplejson
import urllib2

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from config import Config
from models import *

def confirm_melee_kill(request):
    _, lat, lng, _, tar_lat, tar_long = extract_location_data(request)
    dist = get_distance(lat, lng, tar_lat, tar_long)
    if dist < Config.MAX_MELEE_KILL_DIST:
        return HttpResponse("kill")
    else:
        return HttpResponse("nokill")

def confirm_bomb_kill(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)

def plant_bomb(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)
    bomb_type = request.GET('type')
    if bomb_type in ('sticky', 'mine'):
        Bombs.add_bomb(assassin_id, target_id, bomb_type, lat, lng, seconds)

def extract_location_data(request):
    assassin_id = request.GET('fbid')
    lat = request.GET('lat')
    lng = request.GET('lng')
    assassin = Assassin.objects.filter(facebook_id=assassin_id)
    target_id = assassin.get_target_id_display()
    target = Assassin.objects.filter(facebook_id=target_id)
    tar_lat, tar_long = Assassin.get_location(target_id)
    return assassin_id, lat, lng, target_id, tar_lat, tar_long

def get_distance(lat1, lng1, lat2, lng2):
    return sqrt(((lat1-lat2)**2)+((lng1-lng2)**2))

def get_location(request):
    players = Player.objects.all()
    JSON_string = "["
    for player in players:
        JSON_string += "{'fbid':"+player.get_facebook_id_display()+","
        JSON_string += "'name':"+player.get_first_name_display()+","
        JSON_string += "'photo':"+player.get_photo_display()+","
        JSON_string += "'lat':"+player.get_location_lat_display()+","
        JSON_string += "'lng':"+player.get_location_long_display()+"},"
    JSON_string = JSON_string[:-1]+"]"
    return HttpResponse(JSON_string)


def update_location(request):
    assassin_id = request.GET('fbid')
    lat = request.GET('lat')
    lng = request.GET('lng')
    Assassin.update_location(assassin_id, lat, lng)

def new_game(request):
    AssassinSession.add_session(request.GET('name'),
                                request.GET('description'),
                                request.GET('uid'))

def add_new_player(request):
    facebook_id = request.GET('id')
    uri = "http://graph.facebook.com/" + str(facebook_id)
    response = urllib2.urlopen(uri)
    uid = request.GET('id')
    response = simplejson.loads(response)

    Assassin.add_player("590037593", "asdfsadf", "Richie", "Zeng", "Male",
                        "https://fbcdn-profile-a.akamaihd.net/hprofile-ak-snc4/157664_590037593_1292406756_q.jpg")


def add_player_to_game(request):
    player = Assassin.objects.filter(facebook_id=uid)
    game = AssassinSession.objects.filter(session_id=game_id)
    Assassin.update_session(player, game)
    
def game_info(request):
    pass
