from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import  csrf_exempt
from django.shortcuts import render
from .forms import LoginForm, StudentForm
from student.models import Student


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
