from django.contrib import admin
from .models import trips
from .models import load_trips

# Register your models here.

admin.site.register(trips)
admin.site.register(load_trips)