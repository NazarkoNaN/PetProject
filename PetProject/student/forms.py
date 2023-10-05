from django import forms
from django.contrib.auth.models import User
from .models import Student


class StudentCreationForm(forms.Form):
    firstname = forms.CharField(max_length=200, help_text="First name",widget=forms.TextInput(attrs={"class":"form-control","type":"text"}))
    lastname = forms.CharField(max_length=200, help_text="Last name",widget=forms.TextInput(attrs={"class":"form-control","type":"text"}))
    email = forms.EmailField(help_text="name@xample.com",widget=forms.TextInput(attrs={"class":"form-control","type":"email","placeholder":"name@xample.com"}))
    phone = forms.CharField(max_length=12, help_text="123456789",widget=forms.TextInput(attrs={"class":"form-control","type":"text","placeholder":"123456789"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","type":"password","placeholder":"*******"}), help_text="*****")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","type":"password","placeholder":"*******"}), help_text="*****")

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['phone']

