# -*- coding: utf-8 -*-
from django import forms
from .models import Book
from .filechecker import file_size, file_extension

class BookForm(forms.ModelForm):
    pdf = forms.FileField(required=True, validators=[file_size, file_extension])
    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover')

