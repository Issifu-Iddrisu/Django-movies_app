from django.shortcuts import render, get_object_or_404
from .models import Movie
# from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "movies/index.html", {"movies": Movie.objects.all()
                                                 })


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, "movies/detail.html", {"movie": movie})
