from django.contrib import admin

from .models import TeamList, CallBack, Movie
# Register your models here.
admin.site.register(TeamList)
admin.site.register(CallBack)
admin.site.register(Movie)
