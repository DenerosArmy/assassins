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
    facebook_id = request.GET('id')
    uri = "http://graph.facebook.com/" + str(facebook_id)

    pass

def game_info(request):
    #
    pass
