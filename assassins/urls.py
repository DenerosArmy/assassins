from django.conf.urls import patterns, include, url
from views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # Web Services
    url(r'^$', 'assassins.views.home', name='home'),
    url(r'^dashboard', 'assassins.views.dashboard', name='dashboard'),

    # Endpoint Services
    # url(r'^$', 'assassins.views.home', name='home'),
    url(r'^add_new_player', 'assassins.views.add_new_player', name='add_new_player'),
    url(r'^assign_target', 'assassins.views.assign_target', name='assign_target'),
    url(r'^confirm_bomb_kill', 'assassins.views.confirm_bomb_kill', name='confirm_bomb_kill'),
    url(r'^confirm_melee_kill', 'assassins.views.confirm_mellee_kill', name='confirm_melee_kill'),
    url(r'^plant_bomb', 'assassins.views.plant_bomb', name='plant_bomb'),
<<<<<<< HEAD
    url(r'^poll_location', 'assassins.views.poll_location', name='poll_location'),
=======
    url(r'^poll_location', 'assassins.views.get_location', name='poll_location'),
    url(r'^poll_feed', 'assassins.views.get_posts', name='poll_feed'),
>>>>>>> 73ac1e494291efe294d62aeb7c560eb75d980f08
    url(r'^report_kill', 'assassins.views.report_kill', name='report_kill'),
    url(r'^update_location', 'assassins.views.update_player_location', name='update_player_location'),

    # url(r'^assassins/', include('assassins.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
