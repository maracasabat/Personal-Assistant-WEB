from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
@login_required
def homepage(request):
    return render(request, "main/homePage.html")


@login_required
def phonebook_page(request):
    return render(request, "main/phoneBookPage.html")


@login_required
def notebook_page(request):
    return render(request, "main/noteBookPage.html")


@login_required
def gallery_page(request):
    return render(request, "main/galleryPage.html")


@login_required
def settings_page(request):
    return render(request, "main/settingsPage.html")