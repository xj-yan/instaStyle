from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from ins.models import InstaUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = InstaUser
        fields = ('username', 'email', 'profile_pic')

