from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):

    error_css_class = 'btn-outline-danger'
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age',)


class CustomUserChangeForm(UserChangeForm):

    error_css_class = 'btn-outline-danger'
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
