from django.contrib import admin
from .models import Nickname, Name, Surname, Email, Birthday, Country, Address, Happy
# Register your models here.


admin.site.register(Nickname)
admin.site.register(Name)
admin.site.register(Surname)
admin.site.register(Email)
admin.site.register(Birthday)
admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Happy)

