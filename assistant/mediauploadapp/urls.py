

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('books/', views.book_list, name='book_list'),
    path('books/upload/', views.upload_book, name='upload_book'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),

    path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),

    path('photos/', views.photo_list, name='photo_list'),
    path('photodb/clear/', views.clear_database, name='clear_database'),
    path('basicphoto/upload/', views.BasicUploadView.as_view(), name='basic_upload'),
    path('progressbar/upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('draganddrop/upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
]
