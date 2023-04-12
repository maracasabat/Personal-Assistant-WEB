from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from newsapp.views import get_news
from book_app.views import main as phonebook_main
from note_app.views import main as note_main
# from mediauploadapp.views import main as media_main


# Create your views here.
@login_required
def homepage(request):
    # return render(request, "main/homePage.html")
    return redirect(get_news)


@login_required
def phonebook_page(request):
    # return render(request, "main/phoneBookPage.html")
    return redirect(phonebook_main)


@login_required
def notebook_page(request):
    # return render(request, "main/noteBookPage.html")
    return redirect(note_main)


@login_required
def gallery_page(request):
    return render(request, "main/galleryPage.html")
    # return redirect(media_main)


@login_required
def settings_page(request):
    return render(request, "main/settingsPage.html")

@login_required
def team(request):
    return render(request, "main/team.html")


def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session['is_dark_theme'] = not request.session['is_dark_theme']
    else:
        request.session['is_dark_theme'] = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))