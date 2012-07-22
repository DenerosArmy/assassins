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
    
    pass

def add_new_player(request):
    Assassin.add_player(request.GET('uid'),
                      request.GET('access_token'),
                      request.GET('first_name'),
                      request.GET('last_name'),
                      request.GET('gender'),
                      request.GET('photo'),
                      request.GET('admin'))
    """
    facebook_id = request.GET('id')
    uri = "http://graph.facebook.com/" + str(facebook_id)
    response = urllib2.urlopen(uri)

    player = Player.objects.create(facebook_id=facebook_id,
                                   access_token = request.GET('auth_token'))
    """

def add_player_to_game(request):
    player = Assassin.objects.filter(facebook_id=uid)
    game = AssassinSession.objects.filter(session_id=game_id)
    
def game_info(request):
    #
    pass
