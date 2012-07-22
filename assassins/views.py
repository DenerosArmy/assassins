import simplejson
import urllib
import urllib2

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from girl.config import Config
from models import *
from utils import *

def report_kill(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)
    kill(assassin_id)
    assassin_name = Assassin.get(facebook_id=assassin_id).get_first_name
    victim_name = Assassin.get(facebook_id=victim_id).get_first_name
    message = assassin_name+" just killed "+victim_name+"!"
    post_to_feed(message, assassin_id, victim_name)

def confirm_melee_kill(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)
    dist = get_distance(lat, lng, tar_lat, tar_long)
    if dist < Config.MAX_MELEE_KILL_DIST:
        Assassin.kill(assassin_id)
        message = "MELEE! "+assassin_name+" just killed "+victim_name+"!"
        post_to_feed(message, assassin_id, victim_name)
        return HttpResponse("kill")
    else:
        return HttpResponse("nokill")

def confirm_bomb_kill(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)

def plant_bomb(request):
    assassin_id, lat, lng, target_id, tar_lat, tar_long = extract_location_data(request)
    bomb_type = request.GET['type']
    if bomb_type in ('sticky', 'mine'):
        add_bomb(assassin_id, target_id, bomb_type, lat, lng, seconds)

def extract_location_data(request):
    assassin_id = request.GET['fbid']
    lat = request.GET['lat']
    lng = request.GET['lng']
    assassin = Assassin.objects.filter(facebook_id=assassin_id)
    target_id = assassin.get_target_id
    target = Assassin.objects.filter(facebook_id=target_id)
    tar_lat, tar_long = get_location(target_id)
    return assassin_id, lat, lng, target_id, tar_lat, tar_long

def get_distance(lat1, lng1, lat2, lng2):
    return sqrt(((lat1-lat2)**2)+((lng1-lng2)**2))

def get_location(request):
    players = Player.objects.all()
    JSON_string = "["
    for player in players:
        JSON_string += "{'fbid':'"+player.facebook_id+"',"
        JSON_string += "'name':'"+player.first_name+"',"
        JSON_string += "'photo':'"+player.photo+"',"
        JSON_string += "'lat':'"+str(player.location_lat)+"',"
        JSON_string += "'lng':'"+str(player.location_long)+"'},"
    if JSON_string != "[":
        JSON_string = JSON_string[:-1]
    JSON_string += "]"
    return HttpResponse(JSON_string)

def update_player_location(request):
    assassin_id = request.POST['fbid']
    lat = request.POST['lat']
    lng = request.POST['lng']
    update_location(assassin_id, lat, lng)
    return HttpResponse("success")

def new_game(request):
    add_session(request.POST['name'],
                request.POST['description'],
                request.POST['uid'])

def add_new_player(request):
    fbid = request.POST['fbid']
    uri = "http://graph.facebook.com/" + str(fbid)

    result = simplejson.load(urllib.urlopen(uri))

    uid = result['id']
    f_name = result['first_name']
    l_name = result['last_name']
    gender = result['gender']
    username = result['username']
    picture = "http://graph.facebook.com/" + username + "/picture"

    add_player(uid, "auth token", f_name, l_name, gender, picture)
    return HttpResponse(request.POST['fbid'])

def add_player_to_game(request):
    player = Assassin.objects.filter(facebook_id=uid)
    game = AssassinSession.objects.filter(session_id=game_id)
    update_session(player, game)
    
def home(request):
    players = Player.objects.all()
    locations = []
    for player in players:
        location = {}
        location['fbid'] = player.facebook_id
        location['name'] = player.first_name
        location['photo'] = player.photo
        location['lat'] = str(player.location_lat)
        location['long'] = str(player.location_long)
        locations.append(location)
    posts_sets = Feed.get_limit(5)
    posts = []
    for post_set in posts_sets:
        post = {}
        post['fbid'] = post_set.facebook_id
        post['name'] = post_set.first_name
        post['photo'] = post_set.photo
        post['lat'] = str(post_set.location_lat)
        post['lng'] = str(post_set.location_long)
        posts.append(post)
    return render_to_response('home.html', RequestContext(request,{"posts":posts, "locations":locations}))

def dashboard(request):
    return render_to_response('dashboard.html')
