from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import  csrf_exempt
from django.shortcuts import render
from .forms import LoginForm, StudentForm, GenForm
from student.models import Student
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
global cid
import  os

@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print("###############################")
            print(form.data['student_roll'])
            student = Student.objects.get(student_roll=form.data['student_roll'])
            print(student)
            if student:
                if student.password == form.data['password']:
                    return render(request, 'student_dashboard.html', {'name': student.student_name, 's_id': student.student_id, 's_roll':form.data['student_roll']})
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
    if request.method == 'POST':
        form = GenForm(request.POST)
        if form.is_valid():
            print(os.getcwd())
            train = pd.read_excel('student\ModifiedNumericDataSetV2.xlsx', index=False)
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
            curr_student = pd.DataFrame(columns=X.columns)
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
            # curr_student.iloc[0]['10th %']=form.data['percentage_in_10th']
            # curr_student.iloc[0]['10th Board']=form.data['Board_10th']
            # curr_student.iloc[0]['12th %']=form.data['percentage_in_12th']
            # curr_student.iloc[0]['12th Board']=form.data['Board_12th']
            # curr_student.iloc[0]['B. Tech Branch']=form.data['BTech_Branch']
            # curr_student.iloc[0]['Category']=form.data['Category']
            # curr_student.iloc[0]['Date of Birth']=form.data['year_of_birth']
            # curr_student.iloc[0]['Father\'s Occupation']=form.data['Fathers_Occupation']
            # curr_student.iloc[0]['Gender']=form.data['Gender']
            # curr_student.iloc[0]['Mother\'s Occupation']=form.data['Mothers_Occupation']
            # curr_student.iloc[0]['Permanent Address']=form.data['Permanent_address']
            # curr_student.iloc[0]['Year of placement']=form.data['expected_year_of_placement']
            # curr_student.iloc[0]['YoP 10th']=form.data['passing_year_of_10th']
            # curr_student.iloc[0]['YoP 12th']=form.data['passing_year_of_12th']
            # curr_student.iloc[0]['cgpa6']=form.data['current_CGPA']
            # curr_student.iloc[0]['type_dis']=form.data['type_of_disability']

            X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.001, shuffle=False)
            clf = RandomForestClassifier(n_estimators=219
                                         , max_depth=100, random_state=0)
            clf.fit(X_train, y_train)
            print(X_train.columns)
            print(curr_student.columns)
            y_pred = clf.predict(curr_student)
            x = clf.predict_proba(curr_student)
            print(x[0][1])
            return HttpResponse(str(x[0][1]*100)+"% chance of placement")
    else:
        form = GenForm()
    return render(request, 'edit_student_detail.html', {'form': form})
