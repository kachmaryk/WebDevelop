from django import forms
from .models import ContactInfo, OrderInfo
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

class DateInput(forms.DateInput):
    input_type = 'date'

class TripForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['guests', 'acomodation', 'start_date', 'end_date', 'optional']
        widgets = {'start_date': DateInput(), 'end_date': DateInput()}