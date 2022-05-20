from django.db import models
from django.contrib.auth.models import User

#Registration

class Student(User):
    age = models.IntegerField(null=False)
    specialization = models.CharField(max_length = 255)

    def __str__(self):
        return  self.last_name

