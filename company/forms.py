from django import forms
from django.utils.safestring import mark_safe


class CompanyForm(forms.Form):
    company_name = forms.CharField(label=mark_safe('<br />Company Name:'), max_length=1000)
    email_id = forms.CharField(label=mark_safe('<br />Email id:'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password:'), max_length=1000)


class JobForm(forms.Form):
    skills_required = forms.CharField(label=mark_safe('<br />SKILLS REQUIRED (Write all skills space separated):'), max_length=1000)
    ctc = forms.CharField(label=mark_safe('<br />CTC to be Offered:'), max_length=1000)
    date_of_visit = forms.CharField(label=mark_safe('<br />Date of visit:'), max_length=1000)
    openings = forms.CharField(label=mark_safe('<br />Number of openings:'), max_length=1000)
    rounds = forms.CharField(label=mark_safe('<br />Types of rounds  :'), max_length=1000)


class LoginForm(forms.Form):
    company_id = forms.CharField(label=mark_safe('<br />Email id'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password'), max_length=1000)