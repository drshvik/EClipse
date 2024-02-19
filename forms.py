from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        fields = ['username','email','first_name','last_name','password1','password2']
        model = User