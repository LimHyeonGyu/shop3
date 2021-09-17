from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from member.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone']

class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email")

