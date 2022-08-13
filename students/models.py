from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Track(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    birth_date = models.DateField(null=True)
    profile = models.URLField(null=True)
    gender = models.CharField(choices=[
        ("m", "Male"),
        ("f", "Female"),
    ], null=True, max_length=5)
    salary = models.FloatField()
    track = models.ForeignKey(Track, on_delete=models.CASCADE, null=True)
    create_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    create_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    @classmethod
    def get_oldest(cls, number):
        return cls.objects.all()[number]
