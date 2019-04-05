from django import forms
from django.utils.safestring import mark_safe


class StudentForm(forms.Form):
    student_name = forms.CharField(label=mark_safe('<br />Student Name:'), max_length=1000)
    student_id = forms.CharField(label=mark_safe('<br />Email id:'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password:'), max_length=1000)
    student_roll = forms.CharField(label=mark_safe('<br />Roll Number:'), max_length=1000)


class LoginForm(forms.Form):
    student_roll = forms.CharField(label=mark_safe('<br />Login id'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password'), max_length=1000)