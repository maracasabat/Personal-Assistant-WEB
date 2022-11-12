from django.shortcuts import render, redirect
from .models import Book, User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from .forms import BookForm
from django.urls import reverse_lazy

# Create your views here.
class Home(TemplateView):
    template_name = 'mediauploadapp/index.html'

def main(request):
    return render(request, 'mediauploadapp/index.html', {})

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'mediauploadapp/upload.html', context)

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
