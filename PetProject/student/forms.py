from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'type': "username",
        'name': "username",
        'placeholder': "Your username",
        'id': "typeUsernameX",
        'class': "form-control"}))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'type': "email",
        'name': "email",
        'placeholder': "name@xmplae.com",
        'id': "typeEmailX",
        'class': "form-control"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'type': "password",
        'name': "password",
        'id': "typePassword1",
        'class': "form-control"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'type': "password",
        'name': "password",
        'id': "typePassword2",
        'class': "form-control"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "firstname",
        'name': "firstname",
        'id': "typeFirstName",
        'class': "form-control"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'type': "lastname",
        'name': "lastname",
        'id': "typeLastName",
        'class': "form-control"}))
    phone_number = forms.CharField(max_length=12, widget=forms.TextInput(attrs={
        'type': "phone",
        'name': "phone",
        'id': "typePhoneX",
        'class': "form-control"}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        student = Student.objects.create(
            user=user,
            phone=self.cleaned_data['phone_number']
        )
        student.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': "email",
        'id': "typeEmailX",
        'class': "form-control form-control-lg"}))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': "password",
        'id': "typePasswordX",
        'class': "form-control form-control-lg"}))

    def __long__(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.get_latest_by(email=email, password=password)

        if user is not None:
            login(user)

    class Meta:
        model = User
        fields = ['email', 'password']
