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

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise ValidationError(
    #             self.error_messages['password_mismatch'],
    #             code='password_mismatch',
    #         )

    #     return password2


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

    # def clean_pincode(self):
    #     pincode_passed = self.cleaned_data.get("pincode")
