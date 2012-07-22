from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'assassins.views.home', name='home'),
    url(r'^assassins/new_game', 'assassins.views.new_game', name='new_game')
    url(r'^assassins/add_new_player', 'assassins.views.add_new_player', name='new_player')
    url(r'^assassins/add_player_to_game', 'assassins.views.add_player_to_game')

    # url(r'^assassins/', include('assassins.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
