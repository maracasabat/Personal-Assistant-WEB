from django.core.paginator import Paginator
from django.db import IntegrityError
from django.shortcuts import render, redirect

from .models import Tag, Note


# Create your views here.

def main(request):
    notes = Note.objects.all()
    return render(request, 'note_app/index.html', {"notes": notes})

# no work
# def main(request):
#     notes = Note.objects.all()
#     paginator = Paginator(notes, 5)
#
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#
#     return render(request, 'note_app/index.html', {"page_obj": page_obj})


def tag(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            if name:
                tl = Tag(name=name)
                tl.save()
            return redirect(to='/note_app/tag/')
        except ValueError as err:
            return render(request, 'note_app/tag.html', {"error": err})
        # except IntegrityError as err:
        except IntegrityError:
            err = "Tag is exist, try enter another tag..."
            return render(request, 'note_app/tag.html', {"error": err})
    return render(request, 'note_app/tag.html', {})


def note(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        list_tags = request.POST.getlist('tags')
        if name and description:
            tags = Tag.objects.filter(name__in=list_tags)
            note = Note.objects.create(name=name, description=description,)
            for tag in tags.iterator():
                note.tags.add(tag)
        return redirect(to='/note_app/note/')

    tags = Tag.objects.all()
    return render(request, 'note_app/note.html', {"tags": tags})


def detail(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.tag_list = ', '.join([str(name) for name in note.tags.all()])
    return render(request, 'note_app/detail.html', {"note": note})


def set_done(request, note_id):
    Note.objects.filter(pk=note_id).update(done=True)
    return redirect(to='/note_app/')


def delete_note(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect(to='/note_app/')


def search_note(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        notes = Note.objects.filter(name__icontains=query)
    else:
        notes = []
    return render(request, 'note_app/search_note.html', {'notes': notes})
