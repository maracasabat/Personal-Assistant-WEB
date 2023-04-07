from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("phonebook", views.phonebook_page, name="phonebook"),
    path("notebook", views.notebook_page, name="notebook"),
    path("gallery", views.gallery_page, name="gallery"),
    path("team", views.team, name="team"),
    path('switch_theme', views.change_theme, name='change-theme'),

]