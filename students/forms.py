from django import forms
from .models import Student


# class StudentForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     salary = forms.FloatField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ("name", "age", "salary", "email")
