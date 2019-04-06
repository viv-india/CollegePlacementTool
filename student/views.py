from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.views.decorators.csrf import  csrf_exempt
from django.shortcuts import render

from company.models import Job
from .forms import LoginForm, StudentForm, GenForm, CseSkillForm
from student.models import Student, Cse, StudentGen
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os


class StudentId:
    s_id = "NULL"


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(student_roll=form.data['student_roll'])
            StudentId.s_id = form.data['student_roll']
            if student:
                if student.password == form.data['password']:
                    return redirect(student_dashboard)
                else:
                    return HttpResponse("Wrong password")
            else:
                return HttpResponse("Wrong Login Id")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            c_id = form.data['student_roll']
            new_company = Student.objects.create(student_name=form.data['student_name'], student_id=form.data['password'],student_roll=form.data['student_roll'], password=form.data['password'])
            new_company.save()
            return render_to_response('success.html', {'student_id': c_id})
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})


@csrf_exempt
def edit_student_detail(request):
    print("!!!!!!!!!!!!!")
    print(StudentId.s_id)
    if request.method == 'POST':

        form = GenForm(request.POST)
        if form.is_valid() and StudentId.s_id!="NULL":

            try:
                prev_student = StudentGen.objects.filter(student_roll=StudentId.s_id).first()
                if  prev_student:
                 prev_student.delete()
            except StudentGen.DoesNotExist:
                prev_student = None
            new_student_detail = StudentGen.objects.create(percentage_in_10th=form.data['percentage_in_10th'],
                                                           percentage_in_12th=form.data['percentage_in_12th'],
                                                           current_CGPA=form.data['current_CGPA'],
                                                           year_of_birth=form.data['year_of_birth'],
                                                           expected_year_of_placement=form.data[
                                                               'expected_year_of_placement'],
                                                           passing_year_of_10th=form.data['passing_year_of_10th'],
                                                           passing_year_of_12th=form.data['passing_year_of_12th'],
                                                           Board_10th=form.data['Board_10th'],
                                                           Board_12th=form.data['Board_12th'],
                                                           BTech_Branch=form.data['BTech_Branch'],
                                                           Category=form.data['Category'],
                                                           Fathers_Occupation=form.data['Fathers_Occupation'],
                                                           Gender=form.data['Gender'],
                                                           Mothers_Occupation=form.data['Mothers_Occupation'],
                                                           Permanent_address=form.data['Permanent_address'],
                                                           type_of_disability=form.data['type_of_disability'],
                                                           student_roll=StudentId.s_id
                                                           )
            new_student_detail.save()
            print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@##############")

            train = pd.read_excel('ModifiedNumericDataSetV2.xlsx', index=False)
            X = train
            y = train['Placed/Unplaced']
            Y = y
            X = X.drop('Tier', axis=1)
            X = X.drop('cgpa1', axis=1)
            X = X.drop('cgpa2', axis=1)
            X = X.drop('cgpa3', axis=1)
            X = X.drop('cgpa4', axis=1)
            X = X.drop('cgpa5', axis=1)
            X = X.drop('Placed/Unplaced', axis=1)
            list1=[
            (form.data['percentage_in_10th'],
            form.data['Board_10th'],
            form.data['percentage_in_12th'],
            form.data['Board_12th'],
            form.data['BTech_Branch'],
            form.data['Category'],
            form.data['year_of_birth'],
            form.data['Fathers_Occupation'],
            form.data['Gender'],
            form.data['Mothers_Occupation'],
            form.data['Permanent_address'],
            form.data['expected_year_of_placement'],
            form.data['passing_year_of_10th'],
            form.data['passing_year_of_12th'],
            form.data['current_CGPA'],
            form.data['type_of_disability'])
            ]
            list2=[
            '10th %',
            '10th Board',
            '12th %',
            '12th Board',
            'B. Tech Branch',
            'Category',
            'Date of Birth',
            'Father\'s Occupation',
            'Gender',
            'Mother\'s Occupation',
            'Permanent Address',
            'Year of placement',
            'YoP 10th',
            'YoP 12th',
            'cgpa6',
            'type_dis']

            curr_student=pd.DataFrame(list1, columns=list2)

            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.001, shuffle=False)
            clf = RandomForestClassifier(n_estimators=219
                                         , max_depth=100, random_state=0)
            clf.fit(X_train, y_train)
            print(X_train.columns)
            print(curr_student.columns)
            x = clf.predict_proba(curr_student)
            print(x[0][1])
            return redirect(student_dashboard)
    else:
        form = GenForm()
    return render(request, 'edit_student_detail.html', {'form': form})


@csrf_exempt
def student_skill_edit(request):
    print("!!!!!!!!!!!!!")
    print(StudentId.s_id)
    if request.method == 'POST':
        form = CseSkillForm(request.POST)
        if form.is_valid() and StudentId.s_id!="NULL":

            try:
                prev_student = Cse.objects.get(student_roll=StudentId.s_id)
                if prev_student:
                    prev_student.delete()
            except:
                prev_student = None
            new_skill_data= Cse.objects.create(    dsa = form.data['dsa'],
                                                oops = form.data['oops'],
                                                dbms = form.data['dbms'],
                                                Computer_Networks = form.data['network'],
                                                os = form.data['os'],
                                                compiler = form.data['compiler'],
                                                communication = form.data['communication'],
                                                jee_mains = form.data['jee_mains'],
                                                cp = form.data['cp'],
                                                student_roll = StudentId.s_id
                                                 )
            new_skill_data.save()
            return redirect(student_dashboard)
    else:
        form = CseSkillForm()
    return render(request, 'student_skill_edit.html', {'form': form})

@csrf_exempt
def student_dashboard(request):
    print("###################")




    print(StudentId.s_id)



    jobs = Job.objects.all()
    for job in jobs:
        print(job.ctc)

    student = StudentGen.objects.filter(student_roll=StudentId.s_id).first()
    student_skill = Cse.objects.filter(student_roll=StudentId.s_id).first()
    all_student_skills = Cse.objects.all()
    temp_map={}
    temp_map['dsa']=0
    temp_map['oops'] = 0
    temp_map['dbms'] = 0
    temp_map['Computer_Networks'] = 0
    temp_map['os'] = 0
    temp_map['compiler'] = 0
    temp_map['communication'] = 0
    temp_map['jee_mains'] = 0
    temp_map['cp'] = 0
    n=0
    for stuskill in all_student_skills:
        temp_map['dsa'] += stuskill.dsa
        temp_map['oops'] += stuskill.oops
        temp_map['dbms'] += stuskill.dbms
        temp_map['Computer_Networks'] += stuskill.Computer_Networks
        temp_map['os'] += stuskill.os
        temp_map['compiler'] += stuskill.compiler
        temp_map['communication'] += stuskill.communication
        temp_map['jee_mains'] += stuskill.jee_mains
        temp_map['cp'] += stuskill.cp
        n+=1
    temp_map['dsa'] /= n
    temp_map['oops'] /= n
    temp_map['dbms'] /= n
    temp_map['Computer_Networks'] /= n
    temp_map['os'] /= n
    temp_map['compiler'] /= n
    temp_map['communication'] /= n
    temp_map['jee_mains'] /= n
    temp_map['cp'] /= n
    sub_li=[]
    if  student_skill:
        sub_li=[['dsa', student_skill.dsa-temp_map['dsa']],
        ['oops',student_skill.oops - temp_map['oops']],
        ['dbms',student_skill.dbms - temp_map['dbms']],
        ['Computer_Networks',student_skill.Computer_Networks - temp_map['Computer_Networks']],
        ['os',student_skill.os - temp_map['os']],
        ['compiler',student_skill.compiler - temp_map['compiler']],
        ['communication',student_skill.communication - temp_map['communication']],
        ['jee_mains',student_skill.jee_mains - temp_map['jee_mains']],
        ['cp',student_skill.cp - temp_map['cp']],
        ]
    suggestions =[]
    sub_li.sort(key=lambda x: x[1])
    for x in sub_li:
        print(x[1])
        suggestions.append(x[0])
    x=[[None,None]]
    if student:
        train = pd.read_excel('ModifiedNumericDataSetV2.xlsx', index=False)
        X = train
        y = train['Placed/Unplaced']
        Y = y
        X = X.drop('Tier', axis=1)
        X = X.drop('cgpa1', axis=1)
        X = X.drop('cgpa2', axis=1)
        X = X.drop('cgpa3', axis=1)
        X = X.drop('cgpa4', axis=1)
        X = X.drop('cgpa5', axis=1)
        X = X.drop('Placed/Unplaced', axis=1)
        list1 = [
            (student.percentage_in_10th,
             student.Board_10th,
             student.percentage_in_12th,
             student.Board_12th,
             student.BTech_Branch,
             student.Category,
             student.year_of_birth,
             student.Fathers_Occupation,
             student.Gender,
             student.Mothers_Occupation,
             student.Permanent_address,
             student.expected_year_of_placement,
             student.passing_year_of_10th,
             student.passing_year_of_12th,
             student.current_CGPA,
             student.type_of_disability)
        ]
        list2 = [
            '10th %',
            '10th Board',
            '12th %',
            '12th Board',
            'B. Tech Branch',
            'Category',
            'Date of Birth',
            'Father\'s Occupation',
            'Gender',
            'Mother\'s Occupation',
            'Permanent Address',
            'Year of placement',
            'YoP 10th',
            'YoP 12th',
            'cgpa6',
            'type_dis']

        curr_student = pd.DataFrame(list1, columns=list2)

        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.001, shuffle=False)
        clf = RandomForestClassifier(n_estimators=219
                                     , max_depth=100, random_state=0)
        clf.fit(X_train, y_train)
        x = clf.predict_proba(curr_student)
        print(x[0][1])
        print("########")

    return render(request, 'student_dashboard.html', {'pred': x[0][1],'suggestions': suggestions,'jobs':jobs})

