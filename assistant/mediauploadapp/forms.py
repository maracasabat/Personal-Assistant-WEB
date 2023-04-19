# -*- coding: utf-8 -*-
from django import forms
from .models import File, Book, Photo
from .filechecker import file_size, book_size, book_extension


class FileForm(forms.ModelForm):
    file = forms.FileField(required=True, validators=[file_size], widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = File
        fields = ('title', 'file', 'category', 'publication_date')


class BookForm(forms.ModelForm):
    pdf = forms.FileField(required=True, validators=[book_size, book_extension], widget=forms.FileInput(attrs={'class': 'form-control'}))
    cover = forms.FileField(required=True, validators=[file_size], widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ('title', 'author', 'pdf', 'cover', 'publication_date')


class PhotoForm(forms.ModelForm):
    file = forms.FileField(required=True, validators=[file_size], widget=forms.FileInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Photo
        fields = ('file', )