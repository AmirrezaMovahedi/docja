from django import forms
from django.utils import timezone

from .models import *


class UserRegister(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('The username is already exists')
        else:
            return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('The password does not match')
        else:
            return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('The email is duplicate, use another email.')
        else:
            return email


class DoctorRegister(forms.ModelForm):
    CATEGORY_CHOICES = (
        ('پزشک عمومی', 'پزشک عمومی'),
        ('متخصص زیبایی', 'متخصص زیبایی'),
        ('متخصص قلب', 'متخصص قلب'),
        ('متخصص غدد', 'متخصص غدد'),
        ('متخصص زنان', 'متخصص زنان'),
        ('متخصص داخلی', 'متخصص داخلی'),
        ('متخصص گوش،حلق،بینی', 'متخصص گوش،حلق،بینی'),
        ('متخصص داخلی', 'متخصص داخلی'),
        ('جراخ پلاستیک', 'جراخ پلاستیک'),
        ('متخصص اطفال', 'متخصص اطفال'),
        ('متخصص مامایی', 'متخصص مامایی'),
        ('متخصص مغز و اعصاب', 'متخصص مغز و اعصاب'),
        ('دندانپزشک', 'دندانپزشک'),
    )
    expert = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)

    class Meta:
        model = Doctor
        fields = ['photo', 'phone', 'address', 'description', 'mc_number']


class Web_userRegister(forms.ModelForm):
    class Meta:
        model = Web_user
        fields = ['photo', 'phone']


class SearchFrom(forms.Form):
    query = forms.CharField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Doctor_C
        fields = ['message', 'email', 'name']


class UserEdit(forms.ModelForm):
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=20, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError('The username is already exists')
        else:
            return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('The password does not match')
        else:
            return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(id=self.instance.id).filter(email=email).exists():
            raise forms.ValidationError('The email is duplicate, use another email.')
        else:
            return email


class DoctorEdit(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['photo', 'phone', 'address', 'description', 'mc_number']
