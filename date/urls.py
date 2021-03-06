from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from date import settings
# from date_app import urls as profile_urls

urlpatterns = patterns('',
    #ADMIN#
    url(r'^admin/', include(admin.site.urls)),
    #LOGIN AND REGISTER
    url(r'^$', 'django.contrib.auth.views.login', name='login'),
    url(r'^register/$', 'date_app.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    # PASSWORD RESET
    url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    'django.contrib.auth.views.password_reset_confirm',
    name='password_reset_confirm'),
    #SEARCH#
    url(r'^search/$', 'date_app.views.search', name='search'),
    url(r'^search/(?P<coordinates>.*)/$', 'date_app.views.set_lat_long', name='set_lat_long'),
    url(r'^save-lat-long/$', 'date_app.views.save_lat_long', name='save_lat_long'),
    # url(r'^search/(?P<coordinates>.*)/$', 'date_app.views.search_lat_long', name='search_lat_long'),
    #PROFILE#
    url(r'^profile/$', 'date_app.views.profile', name='profile'),
    #DATER PROFILE#
    url(r'^dater_profile/(?P<dater_id>\w+)/$', 'date_app.views.dater_profile', name='dater_profile'),
    url(r'^chat_room/(?P<dater_id>\w+)/$', 'date_app.views.chat_room', name='chat_room'),
    url(r'^chat_messages/(?P<dater_id>\w+)/$', 'date_app.views.chat_messages', name='chat_messages'),
    url(r'^chat_messages_template/(?P<dater_id>\w+)/$', 'date_app.views.chat_messages_template', name='chat_messages_template'),
    url(r'^new_message/$', 'date_app.views.new_message', name='new_message'),
    url(r'^get_names/$', 'date_app.views.get_names', name='get_names'),
    #DATER SEARCH#
    url(r'^date_search/(?P<i>\d+)/$', 'date_app.views.date_search', name='date_search'),
    url(r'^bumped_option/(?P<i>\d+)/(?P<dater>\d+)/(?P<option>\d+)/$', 'date_app.views.bumped_option', name='bumped_option'),
    url(r'^error/$', 'date_app.views.error', name='error'),

)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)