from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from date import settings
from registration import urls as registration_urls
from date_app import urls as profile_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'date.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^register/', include(registration_urls)),
    url(r'^profile/', include(profile_urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),


    # landing pageurl(r'^$', 'date_app.views.home', name='home'),
    url(r'^$', 'date_app.views.home', name='home'),
    url(r'^matches/', 'date_app.views.matches', name='matches'),

    url(r'^purchase', 'registration.views.create_purchase', name='purchase'),

)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)