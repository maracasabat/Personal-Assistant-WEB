from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator

from .models import Nickname, Name, Surname, Email, Birthday, Address, Country, Telephone


# Create your views here.
@login_required
def main(request):
    nicknames = Nickname.objects.filter(author=request.user).all()
    paginator = Paginator(nicknames, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_app/index.html', {"page_obj": page_obj})


@login_required
def contact(request):
    try:
        if request.method == 'POST':
            nickname = request.POST['nickname']
            phone = request.POST['phone']
            if nickname and phone:
                nk = Nickname(nickname=nickname, phone=phone, author=request.user)
                nk.save()
                messages.success(request, "Contact added successfully")
            return redirect(to='/book_app/')
    except IntegrityError:
        messages.error(request, "Data already exists, try enter another phone...")
        # return render(request, 'book_app/contact_err.html', {})
    return render(request, 'book_app/contact.html', {})


@login_required
def nick_edit(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            nickname.nickname = request.POST.get('nickname')
            nickname.phone = request.POST.get('phone')
            nickname.save()
            return redirect(to='/book_app/')
        else:
            return render(request, 'book_app/nick_edit.html', {"nickname": nickname, "phone": phone})
    except IntegrityError:
        err = "Data already exists, try enter another phone..."
        messages.error(request, err)
        return render(request, 'book_app/nick_edit.html', {"nickname": nickname, "phone": phone, "error": err})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def contact_edit(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            telephone = request.POST['telephone']
            name = request.POST['name']
            surname = request.POST['surname']
            email = request.POST['email']
            birthday = request.POST['birthday']
            country = request.POST['country']
            address = request.POST['address']

            if telephone:
                telephone = Telephone()
                telephone.telephone = request.POST.get('telephone')
                telephone.contact_id = nickname_id
                telephone.save()

            if name:
                name_ = Name(pk=nickname_id, name=name, contact_id=nickname_id)
                name_.save()

            if surname:
                surname_ = Surname(pk=nickname_id, surname=surname, contact_id=nickname_id)
                surname_.save()

            if email:
                email_ = Email(pk=nickname_id, email=email, contact_id=nickname_id)
                email_.save()

            if birthday:
                birthday_ = Birthday(pk=nickname_id, birthday=birthday, contact_id=nickname_id)
                birthday_.save()

            if country:
                country_ = Country(pk=nickname_id, country=country, contact_id=nickname_id)
                country_.save()

            if address:
                address_ = Address(pk=nickname_id, address=address, contact_id=nickname_id)
                address_.save()
            return HttpResponseRedirect("/book_app/")
        else:
            return render(request, 'book_app/contact_edit.html', {"nickname": nickname, "phone": phone})
    except IntegrityError:
        err = "Data already exists, try again..."
        messages.error(request, err)
        return render(request, 'book_app/contact_edit.html', {"nickname": nickname, "phone": phone, "error": err})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_name(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            name = request.POST['name']
            if name:
                name_ = Name(pk=nickname_id, name=name, contact_id=nickname_id)
                name_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_name.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_surname(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            surname = request.POST['surname']
            if surname:
                surname_ = Surname(pk=nickname_id, surname=surname, contact_id=nickname_id)
                surname_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_surname.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_email(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            email = request.POST['email']
            if email:
                email_ = Email(pk=nickname_id, email=email, contact_id=nickname_id)
                email_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_email.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_birthday(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            birthday = request.POST['birthday']
            if birthday:
                birthday_ = Birthday(pk=nickname_id, birthday=birthday, contact_id=nickname_id)
                birthday_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_birthday.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_country(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            country = request.POST['country']
            if country:
                country_ = Country(pk=nickname_id, country=country, contact_id=nickname_id)
                country_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_country.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def edit_address(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            address = request.POST['address']
            if address:
                address_ = Address(pk=nickname_id, address=address, contact_id=nickname_id)
                address_.save()
            return detail(request, nickname_id)
        else:
            return render(request, 'book_app/edit_address.html', {"nickname": nickname, "phone": phone})
    except ObjectDoesNotExist:
        return HttpResponseRedirect("/book_app/")


@login_required
def detail(request, nickname_id):
    nickname = Nickname.objects.get(pk=nickname_id)
    phone = Nickname.objects.get(pk=nickname_id)

    try:
        telephones = Telephone.objects.all()
    except ObjectDoesNotExist:
        telephones = None

    try:
        name = Name.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        name = None

    try:
        surname = Surname.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        surname = None

    try:
        email = Email.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        email = None

    try:
        birthday = Birthday.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        birthday = None

    try:
        country = Country.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        country = None

    try:
        address = Address.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        address = None

    return render(request, 'book_app/detail.html',
                  {"nickname": nickname, "phone": phone, "telephones": telephones, "name": name,
                   "surname": surname, "email": email, "birthday": birthday,
                   "country": country, "address": address})


@login_required
def delete_telephone(request, nickname_id, telephone=None):
    try:
        telephone = Telephone.objects.get(telephone=telephone)
        telephone.delete()
    except ObjectDoesNotExist:
        telephone = None

    return detail(request, nickname_id)


@login_required
def delete_name(request, nickname_id):
    try:
        name = Name.objects.get(pk=nickname_id)
        name.delete()
    except ObjectDoesNotExist:
        name = None

    return detail(request, nickname_id)


@login_required
def delete_surname(request, nickname_id):
    try:
        surname = Surname.objects.get(pk=nickname_id)
        surname.delete()
    except ObjectDoesNotExist:
        surname = None

    return detail(request, nickname_id)


@login_required
def delete_email(request, nickname_id):
    try:
        email = Email.objects.get(pk=nickname_id)
        email.delete()
    except ObjectDoesNotExist:
        email = None

    return detail(request, nickname_id)


@login_required
def delete_birthday(request, nickname_id):
    try:
        birthday = Birthday.objects.get(pk=nickname_id)
        birthday.delete()
    except ObjectDoesNotExist:
        birthday = None

    return detail(request, nickname_id)


@login_required
def delete_country(request, nickname_id):
    try:
        country = Country.objects.get(pk=nickname_id)
        country.delete()
    except ObjectDoesNotExist:
        country = None

    return detail(request, nickname_id)


@login_required
def delete_address(request, nickname_id):
    try:
        address = Address.objects.get(pk=nickname_id)
        address.delete()
    except ObjectDoesNotExist:
        address = None

    return detail(request, nickname_id)


@login_required
def delete_all(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        nickname.delete()
    except ObjectDoesNotExist:
        nickname = None

    try:
        phone = Nickname.objects.get(pk=nickname_id)
        phone.delete()
    except ObjectDoesNotExist:
        phone = None

    try:
        telephone = Telephone.objects.get(pk=nickname_id)
        telephone.delete()
    except ObjectDoesNotExist:
        telephone = None

    try:
        name = Name.objects.get(pk=nickname_id)
        name.delete()
    except ObjectDoesNotExist:
        name = None

    try:
        surname = Surname.objects.get(pk=nickname_id)
        surname.delete()
    except ObjectDoesNotExist:
        surname = None

    try:
        email = Email.objects.get(pk=nickname_id)
        email.delete()
    except ObjectDoesNotExist:
        email = None

    try:
        birthday = Birthday.objects.get(pk=nickname_id)
        birthday.delete()
    except ObjectDoesNotExist:
        birthday = None

    try:
        country = Country.objects.get(pk=nickname_id)
        country.delete()
    except ObjectDoesNotExist:
        country = None

    try:
        address = Address.objects.get(pk=nickname_id)
        address.delete()
    except ObjectDoesNotExist:
        address = None

    return redirect(to='/book_app/')


@login_required
def search_contact(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        nicknames = Nickname.objects.filter(
            Q(nickname__icontains=query) | Q(phone__icontains=query)
        ).filter(author=request.user)
    else:
        nicknames = []
    return render(request, 'book_app/search_results.html', {'nicknames': nicknames})


@login_required
def day_to_birthday(request):
    try:
        date_now = datetime.now().date()
        days = []
        all_contacts = Nickname.objects.filter(author=request.user)
        for user in all_contacts:
            users = {}
            users['nickname'] = Nickname.objects.get(pk=user.id)
            users['birthday'] = Birthday.objects.get(pk=user.id)
            date_birth = users['birthday']
            date = datetime(date_now.year, date_birth.birthday.month, date_birth.birthday.day)
            date_n = datetime.strftime(date, '%Y-%m-%d')
            happy = (datetime.strptime(date_n, '%Y-%m-%d') - datetime.strptime(str(date_now), '%Y-%m-%d'))
            if happy.days < 0:
                users['happy'] = happy + timedelta(days=365)
            else:
                users['happy'] = happy
            days.append(users)
        days.sort(key=lambda x: x['happy'])
        return render(request, 'book_app/day_to_birthday.html', {'days': days})
    except ObjectDoesNotExist:
        days = None
        return render(request, 'book_app/day_to_birthday.html', {'days': days})
