from django import forms
from django.utils.safestring import mark_safe


class CseSkillForm(forms.Form):
    oops = forms.CharField(label=mark_safe('<br />Object Oriented Programming:'), max_length=1000)
    dbms = forms.CharField(label=mark_safe('<br />Database and Management Systems:'), max_length=1000)
    network = forms.CharField(label=mark_safe('<br />Computer Networks:'), max_length=1000)
    dsa = forms.CharField(label=mark_safe('<br />Data Structures and Algorithm:'), max_length=1000)
    os = forms.CharField(label=mark_safe('<br />Operating Systems:'), max_length=1000)
    compiler = forms.CharField(label=mark_safe('<br />Compiler:'), max_length=1000)
    cp = forms.CharField(label=mark_safe('<br />Competitive Programming:'), max_length=1000)
    communication = forms.CharField(label=mark_safe('<br />Communication Skills:'), max_length=1000)
    jee_mains = forms.CharField(label=mark_safe('<br />Jee Mains Score:'), max_length=1000)


class StudentForm(forms.Form):
    student_name = forms.CharField(label=mark_safe('<br />Student Name:'), max_length=1000)
    student_id = forms.CharField(label=mark_safe('<br />Email id:'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password:'), max_length=1000)
    student_roll = forms.CharField(label=mark_safe('<br />Roll Number:'), max_length=1000)


class LoginForm(forms.Form):
    student_roll = forms.CharField(label=mark_safe('<br />Login id'), max_length=1000)
    password = forms.CharField(label=mark_safe('<br />Password'), max_length=1000)


class GenForm(forms.Form):
    percentage_in_10th = forms.FloatField()
    percentage_in_12th = forms.FloatField()
    current_CGPA = forms.FloatField()
    year_of_birth = forms.FloatField()
    expected_year_of_placement = forms.FloatField()
    passing_year_of_10th = forms.FloatField()
    passing_year_of_12th = forms.FloatField()
    Board_10th = forms.ChoiceField(choices=
    (
        (1, 'BSEB'),
        (2, 'CBSE'),
        (3, 'ICSE'),
        (4, '10 Other board'),
        (5, 'UP Board'),
        (6, 'RBSE'),
        (7, 'AP Board'),
        (8, 'JAC'),
        (9, 'State Board'),
        (10, 'MP Board'),
        (11, 'SSC'),
    ))

    Board_12th = forms.ChoiceField(choices=
    (
        (1, 'BSEB'),
        (2, 'CBSE'),
        (3, 'UP Board'),
        (4, 'RBSE'),
        (5, 'ISC'),
        (6, '12 Other board'),
        (7, 'NIOS'),
        (8, 'AP Board'),
        (9, 'MP Board'),
        (10, 'ICSE'),
        (11, 'JAC'),
        (12, 'ISCE'),
        (13, 'MPBSE'),
    ))
    BTech_Branch = forms.ChoiceField(choices=
    (
        (1, 'B.Tech-ME'),
        (2, 'B.Tech-EE'),
        (3, 'B.Tech-CE'),
        (4, 'B.Tech-CSE'),
        (5, 'B.Tech-IT'),
        (6, 'B.Arch'),
    ))
    Category = forms.ChoiceField(choices=
    (
        (1, 'General'),
        (2, 'OBC-NCL'),
        (3, 'OBC'),
        (4, 'ST'),
        (5, 'SC'),
        (6, 'OBCPH'),
        (7, 'PH'),
        (8, 'SCPH'),
        (9, 'OBC-NCLPH'),
    ))
    Fathers_Occupation = forms.ChoiceField(choices=
        (
        (2, 'FARMER'),
        (3, 'Doctor'),
        (4, 'Business'),
        (5, 'Other Job'),
        (6, 'GOVERNMENT EMPLOYEE'),
        (7, 'Railway Employee'),
        (8, 'TEACHER'),
        (9, 'GOVERNMENT EMPLOYEEService'),
        (10, 'Service'),
        (11, 'Advocate'),
        (12, 'Professor'),
        (13, 'Bank Manager'),
        (14, 'Retired'),
        (15, 'Private Employee'),
        (16, 'Retired GOVERNMENT EMPLOYEE'),
        (17, 'Engineer'),
        (18, 'PRIVATE Service'),
    ))
    Gender = forms.ChoiceField(choices=
    (
        (1, 'Male'),
        (2, 'Female'),
    ))
    Mothers_Occupation = forms.ChoiceField(choices=
        (
        (2, 'HOUSE WIFE'),
        (3, 'Doctor'),
        (4, 'Mother Other Job'),
        (5, 'TEACHER'),
        (6, 'GOVERNMENT EMPLOYEE'),
        (7, 'Business'),
    ))
    Permanent_address = forms.ChoiceField(choices=
    (
        (1, 'Rural'),
        (2, 'Urban'),
    ))
    type_of_disability = forms.ChoiceField(choices=
    (
        (1, 'NO_DIS'),
        (2, 'Specially Abled'),
    ))