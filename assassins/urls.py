from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'assassins.views.home', name='home'),
    url(r'^add_new_player', 'assassins.views.add_new_player', name='add_new_player'),
    url(r'^update_location', 'assassins.views.update_location', name='update_location'),
    url(r'^poll_location', 'assassins.views.get_location', name='poll_location'),
    url(r'^confirm_melee_kill', 'assassins.views.confirm_mellee_kill', name='confirm_melee_kill'),
    url(r'^confirm_bomb_kill', 'assassins.views.confirm_bomb_kill', name='confirm_bomb_kill'),
    url(r'^plant_bomb', 'assassins.views.plant_bomb', name='plant_bomb'),
    # url(r'^assassins/', include('assassins.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
