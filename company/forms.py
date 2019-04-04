from django import forms
from django.utils.safestring import mark_safe


class NameForm(forms.Form):
    company_name = forms.CharField(label = mark_safe('<br />Company Name'), max_length=100)
    skills_required = forms.CharField(label = mark_safe('<br /><br />SKILLS REQUIRED (Write all skills space separated)'), max_length=100)
    ctc = forms.CharField(label = mark_safe('<br /><br />CTC OFFERED'), max_length=100)
