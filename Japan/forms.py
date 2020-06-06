from django import forms
from .models import ContactInfo
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = [
            'title',
            'name',
            'description'
        ]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
