from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('search_result/',  views.search_contact, name='search_results'),
    path('contact_err/', views.contact, name='contact'),
    path('info_err/', views.info, name='info'),
    path('detail/<int:nickname_id>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('contact_edit/<int:nickname_id>', views.contact_edit, name='contact_edit'),
    path('nick_edit/<int:nickname_id>', views.nick_edit, name='nick_edit'),
    path('info/<int:nickname_id>', views.info, name='info'),
    path('delete_all/<int:nickname_id>', views.delete_all, name='delete_all'),
    path('day_to_birthday/', views.day_to_birthday, name='day_to_birthday')
]
