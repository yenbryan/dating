from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'registration.views.profile', name='profile'),
)