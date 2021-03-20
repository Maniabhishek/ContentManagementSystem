from django.contrib.auth.forms import UserCreationForm
from django.forms import models
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile


class CreateUser_Register(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'password1', 'password2')

# this is profile form we are using it to store the phone and pin , all the field level validation is done in api


class ProfileForm(forms.ModelForm):
    phone = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'autocomplete': 'off', 'pattern': '[0-9]+', 'title': 'only number'}))

    class Meta:
        model = Profile
        fields = ['phone', 'pincode']

    def clean_phone(self):
        phone_passed = self.cleaned_data.get("phone")
        if len(phone_passed) < 10:
            print("INVALID PHONE")
            raise forms.ValidationError("Please check the number you entered")
        elif len(phone_passed) > 10:
            raise forms.ValidationError(
                "Check the phone number too many digits")
        return phone_passed
