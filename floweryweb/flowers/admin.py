from django.contrib import admin

from .models import Members, Flowers, Features, Sightings

admin.site.register(Members)
admin.site.register(Flowers)
admin.site.register(Features)
admin.site.register(Sightings)
