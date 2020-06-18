from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True, label='Email')

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']



            
    # def save(self, commit=True):
    #     user = super(UserCreationForm, self).save(commit=False)
    #     user.email = self.cleaned_data["email"]
    #     if commit:
    #         user.save()
    #     return user