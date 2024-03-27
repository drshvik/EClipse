from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['username','email','first_name','last_name','password1','password2']
        model = User

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("Please enter a valid email address.")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'image']