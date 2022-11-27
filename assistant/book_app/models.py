import re
from datetime import date

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator, EmailValidator

from django.db import models


class Nickname(models.Model):
    nickname = models.CharField(max_length=150, null=False, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(validators=[RegexValidator(
        regex=r"^\+?1?\d{8,15}$",
        message="input correct phone",
        code="invalid",
        inverse_match=False,
        flags=re.IGNORECASE
    )], max_length=16, null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nickname


class Telephone(models.Model):
    telephone = models.CharField(validators=[RegexValidator(
        regex=r"^\+?1?\d{8,15}$",
        message="input correct phone",
        code="invalid",
        inverse_match=False,
        flags=re.IGNORECASE
    )], max_length=16, blank=True, null=True)
    # telephone = models.TextField(blank=True, null=True, unique=True)
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='telephones')

    def __str__(self):
        return f'{self.telephone}'

    # def all_phones_to_string(self):
    #     return ", ".join([telephone.telephone for telephone in self.telephones.all()])
    #


class Name(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='names')
    name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name


class Surname(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='surnames')
    surname = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.surname


class Email(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='emails')
    email = models.CharField(max_length=50, null=True, blank=True, validators=[
        EmailValidator(
            message='input correct email'
        )
    ])

    def __str__(self):
        return f"{self.email}"


class Birthday(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name="birthdays")
    birthday = models.DateField(default=date.today, null=True)

    def __str__(self):
        return f'{self.birthday}'


class Country(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='countrys')
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country


class Address(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.address
