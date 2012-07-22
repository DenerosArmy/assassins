import simplejson
import urllib2

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import *

def kill_confirm(request):
    killed = True
    # confirm location
    # if accelerometer kill
    # if camera kill
    # if voice kill
    # update shit if the kill was confirmed
    if killed:
        killer = Assassin.objects.filter(facebook_id=request.GET('id')
        killer.target = killer.target.target


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

    Assassin.add_player(response['uid'],
                        #blahblahblah)

def add_player_to_game(request):
    player = Assassin.objects.filter(facebook_id=uid)
    game = AssassinSession.objects.filter(session_id=game_id)
    Assassin.update_session(player, game)
    
def game_info(request):
    pass
