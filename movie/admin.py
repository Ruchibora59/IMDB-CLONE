from django.contrib import admin

from movie.models import Movie, Review

from newmovies.models import Upcoming
# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Upcoming)