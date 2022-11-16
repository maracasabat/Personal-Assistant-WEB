from django.urls import path
from . import views

urlpatterns = [
    # path('', views.main, name='main'),
    path('news/', views.get_news, name='news'),
    path('sport/', views.get_sport_news, name='sport'),
    path('currency/', views.get_currency, name='currency'),
    path('it/', views.get_it, name='it'),
    path('fashion/', views.get_fashion, name='fashion'),
    path('books/', views.get_books, name='books'),
]
