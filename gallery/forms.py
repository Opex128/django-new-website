from django import forms

from django.contrib.auth.models import User
from .models import Profile, Post


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["photo"]


from django_ckeditor_5.fields import CKEditor5Field


class PostForm(forms.ModelForm):
    # Используем CKEditor5Field для поля body
    body = CKEditor5Field()

    class Meta:
        model = Post
        fields = ["title", "preview", "body", "link", "image"]
