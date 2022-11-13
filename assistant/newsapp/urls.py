from django.urls import path
from . import views

urlpatterns = [
    path('news/', views.get_news, name='news'),
    path('sport/', views.get_sport_news, name='sport'),
]
