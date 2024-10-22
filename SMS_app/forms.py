from django import forms
from django.contrib.auth.forms import UserCreationForm

from SMS_app.models import User, Teacher, Student


class UserReg(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model= User
        fields = ('username','password1','password2')

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        exclude=('user',)

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        exclude=("user",)