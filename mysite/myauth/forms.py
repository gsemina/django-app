from django import forms

from django.contrib.auth.models import User

from .models import Profile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name']

