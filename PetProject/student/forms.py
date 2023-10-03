from django import forms

class StudentForm(forms.Form):
    firstname = forms.CharField()
    lastname = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField(max_length=12)
