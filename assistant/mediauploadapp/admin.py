from django.contrib import admin
from .models import File, Book

# Register your models here.

admin.site.register(File)
admin.site.register(Book)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ('doc_name',)
#
# admin.site.register(Document, DocumentAdmin)