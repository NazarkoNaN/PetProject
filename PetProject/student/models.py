from django.contrib.auth.models import User
from django.db import models
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.IntegerField(default=1)
    phone = models.CharField(max_length=12, default=None)
    def __str__(self):
        return self.user