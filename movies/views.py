from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Comment, Like

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, id):
    movie = get_object_or_404(Movie, id=id)

    if request.method == 'POST':
        Comment.objects.create(
            movie=movie,
            user=request.user,
            text=request.POST['text']
        )
        return redirect('movie_detail', id=id)

    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def like_movie(request, id):
    movie = get_object_or_404(Movie, id=id)
    Like.objects.get_or_create(movie=movie, user=request.user)
    return redirect('movie_detail', id=id)
