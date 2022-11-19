from django.contrib import admin
# from .models import Nickname, Name, Surname, Email, Birthday, Country, Address
from .models import Nickname, Name, Surname, Email, Birthday, Country, Address, Telephone
# Register your models here.


admin.site.register(Nickname)
admin.site.register(Name)
admin.site.register(Surname)
admin.site.register(Email)
admin.site.register(Birthday)
admin.site.register(Country)
admin.site.register(Address)

admin.site.register(Telephone)

