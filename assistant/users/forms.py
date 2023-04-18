from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=50, min_length=4, strip=True, widget=forms.TextInput(attrs={ 'style': 'width: 100%; background-color: #ffffff11;  '
                                                            'padding: 0 10px;  color: #fff;  border-radius: 5px; '
                                                            'height: 40px; focus:outline-none; focus:ring-2; '
                                                            'focus:ring-purple-600; focus:border-transparent;' }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={  'style': 'width: 100%; background-color: #ffffff11;  '
                                                            'padding: 0 10px;  color: #fff;  border-radius: 5px; '
                                                            'height: 40px; focus:outline-none; focus:ring-2; '
                                                            'focus:ring-purple-600; focus:border-transparent;'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={  'style': 'width: 100%; background-color: #ffffff11;  '
                                                            'padding: 0 10px;  color: #fff;  border-radius: 5px; '
                                                            'height: 40px; focus:outline-none; focus:ring-2; '
                                                            'focus:ring-purple-600; focus:border-transparent;'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={ 'style': 'width: 100%; background-color: #ffffff11;  '
                                                            'padding: 0 10px;  color: #fff;  border-radius: 5px; '
                                                            'height: 40px; focus:outline-none; focus:ring-2; '
                                                            'focus:ring-purple-600; focus:border-transparent;'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={  'style': 'width: 100%; background-color: #ffffff11;  '
                                                            'padding: 0 10px;  color: #fff;  border-radius: 5px; '
                                                            'height: 40px; focus:outline-none; focus:ring-2; '
                                                            'focus:ring-purple-600; focus:border-transparent;'}),
        label="Username or Email")

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={ 'style': 'width: 100%; background-color: #ffffff11;  padding: 0 10px; color: #fff;   border-radius: 5px; height: 40px;'}),
        label="Password")


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={
            'class': 'py-2 px-3 rounded-lg border-2 border-purple-300 mt-1 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent w-full'}))
    first_name = forms.CharField(
        label='First name', required=False, widget=forms.TextInput(attrs={
            'class': 'py-2 px-3 rounded-lg border-2 border-purple-300 mt-1 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent w-full'}))
    last_name = forms.CharField(
        label='Last name', required=False, widget=forms.TextInput(attrs={
            'class': 'py-2 px-3 rounded-lg border-2 border-purple-300 mt-1 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparent w-full'}))
    description = forms.CharField(label='Description', required=False, widget=forms.Textarea(attrs={
        'class': 'py-2 px-3 rounded-lg border-2 border-purple-300 mt-1 focus:outline-none focus:ring-2 focus:ring-purple-600 focus:border-transparen w-full h-20 resize-none', }))
    avatar = forms.ImageField(label='', required=False, widget=forms.FileInput(attrs={
        'class': 'hidden', 'id': 'avatar'}))

    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name', 'description', 'avatar']