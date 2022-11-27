from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('search_result/',  views.search_contact, name='search_results'),
    path('contact_err/', views.contact, name='contact'),

    path('detail/<int:nickname_id>', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
    path('contact_edit/<int:nickname_id>', views.contact_edit, name='contact_edit'),

    path('nick_edit/<int:nickname_id>', views.nick_edit, name='nick_edit'),

    path('delete_all/<int:nickname_id>', views.delete_all, name='delete_all'),
    path('day_to_birthday/', views.day_to_birthday, name='day_to_birthday'),

    path('delete_telephone/<int:nickname_id>/<telephone>', views.delete_telephone, name='delete_telephone'),
    path('delete_name/<int:nickname_id>', views.delete_name, name='delete_name'),
    path('delete_surname/<int:nickname_id>', views.delete_surname, name='delete_surname'),
    path('delete_email/<int:nickname_id>', views.delete_email, name='delete_email'),
    path('delete_birthday/<int:nickname_id>', views.delete_birthday, name='delete_birthday'),
    path('delete_country/<int:nickname_id>', views.delete_country, name='delete_country'),
    path('delete_address/<int:nickname_id>', views.delete_address, name='delete_address'),

    # path('edit_telephone/<int:nickname_id>', views.edit_telephone, name='edit_telephone'),
    path('edit_name/<int:nickname_id>', views.edit_name, name='edit_name'),
    path('edit_surname/<int:nickname_id>', views.edit_surname, name='edit_surname'),
    path('edit_email/<int:nickname_id>', views.edit_email, name='edit_email'),
    path('edit_birthday/<int:nickname_id>', views.edit_birthday, name='edit_birthday'),
    path('edit_country/<int:nickname_id>', views.edit_country, name='edit_country'),
    path('edit_address/<int:nickname_id>', views.edit_address, name='edit_address'),

]
