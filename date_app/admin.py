from django.contrib import admin
from date_app.models import Match, Image, Dater

admin.site.register(Dater)
admin.site.register(Image)
admin.site.register(Match)