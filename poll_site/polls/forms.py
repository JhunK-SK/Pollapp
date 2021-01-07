from django import forms
from .models import Poll
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'option_one', 'option_two', 'option_three']
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        