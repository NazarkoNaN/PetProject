from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.db import models


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.IntegerField(default=1)
    phone = models.CharField(max_length=12, default=None)
    def __str__(self):
        return self.user

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None