from django.contrib import admin
from .models import Book

# Register your models here.
# admin.site.register(File)
# admin.site.register(Tag)
# admin.site.register(Document)
# admin.site.register(Movie)
admin.site.register(Book)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ('doc_name',)
#
# admin.site.register(Document, DocumentAdmin)