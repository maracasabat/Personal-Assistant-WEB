import re
from datetime import date
from django.core.validators import RegexValidator, EmailValidator

from django.db import models


class Nickname(models.Model):
    nickname = models.CharField(max_length=150, unique=True, null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname


class Phone(models.Model):
    phone = models.CharField(validators=[RegexValidator(
        regex=r"^\+?1?\d{8,15}$",
        message="input correct phone",
        code="invalid",
        inverse_match=False,
        flags=re.IGNORECASE
    )], max_length=16, unique=True)
    # phone = PhoneNumberField(blank=True)
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='phones')


    def __str__(self):
        return f'{self.phone}'


class Name(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='names')
    name = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.name


class Surname(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='surnames')
    surname = models.CharField(max_length=150, null=True)

    def __str__(self):
        return self.surname


class Email(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='email')
    email = models.CharField(max_length=50, unique=False, null=True, validators=[
        EmailValidator(
            message='input correct email'
        )
    ])

    def __str__(self):
        return f"{self.email}"


class Birthday(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name="birthday")
    birthday = models.DateField(default=date.today, null=True)

    def __str__(self):
        return f'{self.birthday}'


class Country(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='countrys')
    country = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.country


class Address(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField(null=True)

    def __str__(self):
        return self.address


class Happy(models.Model):
    contact = models.ForeignKey(Nickname, null=True, blank=True, on_delete=models.CASCADE, related_name='happys')
    happy = models.CharField(max_length=2, null=True)

    def __str__(self):
        return self.happy
