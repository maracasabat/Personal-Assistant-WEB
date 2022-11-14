from django.shortcuts import render, redirect
from .models import File, Book, User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from .forms import FileForm, BookForm
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'mediauploadapp/index.html'

def main(request):
    return render(request, 'mediauploadapp/index.html', {})


""" Add method for the simple upload """

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'mediauploadapp/upload.html', context)


""" Add methods for the file upload """


def file_list(request):
    files = File.objects.all()
    return render(request, 'mediauploadapp/file_list.html', {
        'files': files
    })


def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('file_list')
    else:
        form = FileForm()
    return render(request, 'mediauploadapp/upload_file.html', {
        'form': form
    })


def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


""" Add methods for the book upload """


def book_list(request):
    books = Book.objects.all()
    return render(request, 'mediauploadapp/book_list.html', {
        'books': books
    })


def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'mediauploadapp/upload_book.html', {
        'form': form
    })


def delete_book(request, pk):
    if request.method == 'POST':
        book = Book.objects.get(pk=pk)
        book.delete()
    return redirect('book_list')


class UploadBookView(CreateView):
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('class_book_list')
    template_name = 'mediauploadapp/upload_book.html'
