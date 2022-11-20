from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import File, Book, Photo, User
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.generic import TemplateView, ListView, CreateView
from django.views import View
from .forms import FileForm, BookForm, PhotoForm
from django.urls import reverse_lazy


# Create your views here.
class Home(TemplateView):
    template_name = 'mediauploadapp/index.html'


@login_required
def main(request):
    return render(request, 'mediauploadapp/index.html', {})


""" Add method for the simple upload """


@login_required
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'mediauploadapp/upload.html', context)


""" Add methods for the file upload """


@login_required
def file_list(request):
    files = File.objects.all()
    return render(request, 'mediauploadapp/file_list.html', {
        'files': files
    })


@login_required
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


@login_required
def delete_file(request, pk):
    if request.method == 'POST':
        file = File.objects.get(pk=pk)
        file.delete()
    return redirect('file_list')


""" Add methods for the book upload """


@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'mediauploadapp/book_list.html', {
        'books': books
    })


@login_required
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


@login_required
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


""" Add methods for the photos upload """


@login_required
def photo_list(request):
    books = Photo.objects.all()
    return render(request, 'mediauploadapp/photo_list.html', {
        'books': books
    })


class BasicUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'mediauploadapp/basic_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class ProgressBarUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'mediauploadapp/progress_bar_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


class DragAndDropUploadView(View):
    def get(self, request):
        photos_list = Photo.objects.all()
        return render(self.request, 'mediauploadapp/drag_and_drop_upload_photo.html', {'photos': photos_list})

    def post(self, request):
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


@login_required
def clear_database(request):
    for photo in Photo.objects.all():
        photo.file.delete()
        photo.delete()
    return redirect(request.POST.get('next'))
