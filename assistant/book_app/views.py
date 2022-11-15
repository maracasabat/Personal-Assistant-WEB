from datetime import datetime

from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Nickname, Name, Surname, Email, Birthday, Address, Country, Happy


# Create your views here.
def main(request):
    nicknames = Nickname.objects.all()
    return render(request, 'book_app/index.html', {"nicknames": nicknames})


def contact(request):
    try:
        if request.method == 'POST':
            nickname = request.POST['nickname']
            phone = request.POST['phone']
            if nickname and phone:
            # if nickname:
                nk = Nickname(nickname=nickname, phone=phone)
                nk.save()
            # if phone:
            #     ph = Nickname(phone=phone)
            #     ph.save()
            return redirect(to='/book_app/')
    except IntegrityError:
        return render(request, 'book_app/contact_err.html', {})
    return render(request, 'book_app/contact.html', {})


def info(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            name = request.POST['name']
            surname = request.POST['surname']
            email = request.POST['email']
            birthday = request.POST['birthday']
            country = request.POST['country']
            address = request.POST['address']

            if name:
                name_ = Name(pk=nickname_id, name=name)
                name_.save()

            if surname:
                surname_ = Surname(pk=nickname_id, surname=surname)
                surname_.save()

            if email:
                email_ = Email(pk=nickname_id, email=email)
                email_.save()

            if birthday:
                birthday_ = Birthday(pk=nickname_id, birthday=birthday)
                birthday_.save()

                date_lst = birthday.split('-')
                today = datetime.now().date()
                year_n = datetime.now().year
                date_birth = datetime(year=int(date_lst[0]), month=int(date_lst[1]),
                                      day=int(date_lst[2])).date().replace(year=int(year_n))
                happy = (date_birth - today).days
                Happy.objects.create(id=nickname_id, happy=happy)

            if country:
                country_ = Country(pk=nickname_id, country=country)
                country_.save()

            if address:
                address_ = Address(pk=nickname_id, address=address)
                address_.save()
            return HttpResponseRedirect("/book_app/")
        else:
            return render(request, 'book_app/info.html', {"nickname": nickname, "phone": phone})
    except Nickname.DoesNotExist:
        return HttpResponseNotFound("<h2>Not found</h2>")

#
# def contact_edit(request, nickname_id):
#     try:
#         nickname = Nickname.objects.get(pk=nickname_id)
#         phone = Nickname.objects.get(pk=nickname_id)
#         name = Name.objects.get(pk=nickname_id)
#         surname = Surname.objects.get(pk=nickname_id)
#         email = Email.objects.get(pk=nickname_id)
#         birthday = Birthday.objects.get(pk=nickname_id)
#         country = Country.objects.get(pk=nickname_id)
#         address = Address.objects.get(pk=nickname_id)
#
#         if nickname or phone:
#             Nickname.objects.create(id=nickname_id, nickname=nickname)
#             Nickname.objects.create(pk=nickname_id, phone=phone)
#         else:
#             if request.method == 'POST':
#                 nickname = request.POST['nickname']
#                 phone = request.POST['phone']
#                 if nickname or phone:
#                     nickname_ = Nickname(pk=nickname_id, nickname=nickname)
#                     nickname_.save()
#                     phone_ = Nickname(pk=nickname_id, phone=phone)
#                     phone_.save()
#
#         if name or surname or email or birthday or country or address:
#             Name.objects.create(id=nickname_id, name=name)
#             Surname.objects.create(pk=nickname_id, surname=surname)
#             Email.objects.create(id=nickname_id, email=email)
#             Birthday.objects.create(pk=nickname_id, birthday=birthday)
#             Country.objects.create(id=nickname_id, country=country)
#             Address.objects.create(pk=nickname_id, address=address)
#         else:
#             if request.method == 'POST':
#                 name = request.POST['name']
#                 surname = request.POST['surname']
#                 email = request.POST['email']
#                 birthday = request.POST['birthday']
#                 country = request.POST['country']
#                 address = request.POST['address']
#                 if name or surname or email or birthday or country or address:
#                     name_ = Nickname(pk=nickname_id, nickname=nickname)
#                     name_.save()
#                     surname_ = Nickname(pk=nickname_id, phone=phone)
#                     surname_.save()
#                     email_ = Nickname(pk=nickname_id, nickname=nickname)
#                     email_.save()
#                     birthday_ = Nickname(pk=nickname_id, phone=phone)
#                     birthday_.save()
#                     country_ = Nickname(pk=nickname_id, nickname=nickname)
#                     country_.save()
#                     address_ = Nickname(pk=nickname_id, phone=phone)
#                     address_.save()
#
#         return render(request, 'book_app/contact_edit.html', {"nickname": nickname, "phone": phone, "name": name,
#                                                           "surname": surname, "email": email, "birthday": birthday,
#                                                           "country": country, "address": address})
#     except ObjectDoesNotExist:
#         return HttpResponseRedirect("/book_app/")


def contact_edit(request, nickname_id):
    try:
        nickname = Nickname.objects.get(pk=nickname_id)
        phone = Nickname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            nickname = request.POST.get('nickname')
            phone = request.POST.get('phone')
            if nickname or phone:
                nickname = Nickname(pk=nickname_id, nickname=nickname)
                nickname.save()
                phone = Nickname(pk=nickname_id, phone=phone)
                phone.save()
    except ObjectDoesNotExist:
        nickname = None
        phone = None
        if request.method == 'POST':
            nickname = request.POST['nickname']
            phone = request.POST['phone']
            if nickname or phone:
                nickname_ = Nickname(pk=nickname_id, nickname=nickname)
                nickname_.save()
                phone_ = Nickname(pk=nickname_id, phone=phone)
                phone_.save()

    try:
        name = Name.objects.get(pk=nickname_id)
        if request.method == 'POST':
            name.name = request.POST.get('name')
            name.save()
    except ObjectDoesNotExist:
        name = None
        if request.method == 'POST':
            name = request.POST['name']
            if name:
                name_ = Name(pk=nickname_id, name=name)
                name_.save()

    try:
        surname = Surname.objects.get(pk=nickname_id)
        if request.method == 'POST':
            surname.surname= request.POST.get('surname')
            surname.save()
    except ObjectDoesNotExist:
        surname = None
        if request.method == 'POST':
            surname = request.POST['surname']
            if surname:
                surname_ = Email(pk=nickname_id, surname=surname)
                surname_.save()

    try:
        email = Email.objects.get(pk=nickname_id)
        if request.method == 'POST':
            email.email = request.POST.get('email')
            email.save()
    except ObjectDoesNotExist:
        email = None
        if request.method == 'POST':
            email = request.POST['email']
            if email:
                email_ = Email(pk=nickname_id, email=email)
                email_.save()

    try:
        birthday = Birthday.objects.get(pk=nickname_id)
        if request.method == 'POST':
            birthday.birthday = request.POST.get('birthday')
            birthday.save()
    except ObjectDoesNotExist:
        birthday = None
        if request.method == 'POST':
            birthday = request.POST.get('birthday')
            if birthday:
                birthday_ = Birthday(pk=nickname_id, birthday=birthday)
                birthday_.save()

    try:
        country = Country.objects.get(pk=nickname_id)
        if request.method == 'POST':
            country.country = request.POST.get('country')
            country.save()
    except ObjectDoesNotExist:
        country = None
        if request.method == 'POST':
            country = request.POST['country']
            if country:
                country_ = Country(pk=nickname_id, country=country)
                country_.save()

    try:
        address = Address.objects.get(pk=nickname_id)
        if request.method == 'POST':
            address.address = request.POST.get('address')
            address.save()
    except ObjectDoesNotExist:
        address = None
        if request.method == 'POST':
            address = request.POST['address']
            if country and address:
                address_ = Address(pk=nickname_id, address=address)
                address_.save()

    return render(request, 'book_app/contact_edit.html',
                  {"nickname": nickname, "phone": phone, "name": name, "surname": surname, "email": email,
                   "birthday": birthday, "country": country, "address": address})


def detail(request, nickname_id):
    nickname = Nickname.objects.get(pk=nickname_id)
    phone = Nickname.objects.get(pk=nickname_id)

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
        happy = Happy.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        happy = None

    try:
        country = Country.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        country = None

    try:
        address = Address.objects.get(pk=nickname_id)
    except ObjectDoesNotExist:
        address = None

    return render(request, 'book_app/detail.html', {"nickname": nickname, "phone": phone, "name": name,
                                                    "surname": surname, "email": email, "birthday": birthday,
                                                    "happy": happy, "country": country, "address": address})


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
        happy = Happy.objects.get(pk=nickname_id)
        happy.delete()
    except ObjectDoesNotExist:
        happy = None

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


def search_contact(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        nicknames = Nickname.objects.filter(nickname__icontains=query)
    else:
        nicknames = []
    return render(request, 'book_app/search_results.html', {'nicknames': nicknames})


# def day_to_birthday(request):
    # try:
    #     nicknames = Nickname.objects.all()
    #     for nickname in nicknames:
    #         nickname = Nickname.objects.get(pk=nickname.id)
    #     birthdays = Birthday.objects.all()
    #     for birthday in birthdays:
    #         birthday = Birthday.objects.get(pk=nickname.id)
    #     happys = Happy.objects.all()
    #     for happy in happys:
    #         happy = Happy.objects.get(pk=nickname.id)
    #
    #     if nickname.id == birthday.id == happy.id:
    #         return render(request, 'book_app/day_to_birthday.html', {'nicknames': nicknames, "birthday": birthday,
    #                                                                      "happy": happy})
    # except Nickname.DoesNotExist:
    #     return render(request, 'book_app/day_to_birthday.html', {})


# def day_to_birthday(request):
#     try:
#         nicknames = Nickname.objects.all()
#         if nicknames:
#             for nickname in nicknames:
#                 try:
#                     birthday = Birthday.objects.get(pk=nickname.id)
#                     happy = Happy.objects.get(pk=nickname.id)
#                     return render(request, 'book_app/day_to_birthday.html', {'nicknames': nicknames,
#                                                                              "birthday": birthday,
#                                                                              "happy": happy})
#                 except ObjectDoesNotExist:
#                     return render(request, 'book_app/day_to_birthday.html', {'nicknames': nicknames})
#
#     except Nickname.DoesNotExist:
#         return render(request, 'book_app/day_to_birthday.html', {})

# 2
# def day_to_birthday(request):
#     days = []
#     try:
#         nicknames = Nickname.objects.all()
#         for nickname in nicknames:
#             try:
#                 # name = Name.objects.get(pk=nickname.id)
#                 birthday = Birthday.objects.get(pk=nickname.id)
#                 happy = Happy.objects.get(pk=nickname.id)
#                 # days.append(name)
#                 days.append(birthday)
#                 days.append(happy)
#                 return render(request, 'book_app/day_to_birthday.html', {'days': days})
#             except Birthday.DoesNotExist:
#                 return render(request, 'book_app/day_to_birthday.html', {})
#     except Nickname.DoesNotExist:
#         return render(request, 'book_app/day_to_birthday.html', {})

def day_to_birthday(request):
    try:
        days = []
        all_contacts = Nickname.objects.all()
        for user in all_contacts:
            try:
                users = {}
                users['nickname'] = Nickname.objects.get(pk=user.id)
                users['birthday'] = Birthday.objects.get(pk=user.id)
                users['happy'] = Happy.objects.get(pk=user.id)
                days.append(users)
            except Birthday.DoesNotExist:
                users['nickname'] = None
                return render(request, 'book_app/day_to_birthday.html', {'days': days})
    except Nickname.DoesNotExist:
        return render(request, 'book_app/day_to_birthday.html', {})
