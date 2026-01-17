from django.urls import path
from . import views

urlpatterns = [
    # Главная страница — список фильмов
    path('', views.movie_list, name='movie_list'),

    # Альтернативный URL для списка фильмов
    path('movies/', views.movie_list, name='movies'),

    # Страница одного фильма
    path('movie/<int:id>/', views.movie_detail, name='movie_detail'),

    # Лайк фильма
    path('like/<int:id>/', views.like_movie, name='like_movie'),
]
