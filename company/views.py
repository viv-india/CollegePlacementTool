from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import  csrf_exempt
from django.shortcuts import render
from .forms import LoginForm, JobForm, CompanyForm
from company.models import Company, Job
import uuid


@csrf_exempt
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            company = Company.objects.get(company_id=form.data['company_id'])
            if company:
                if company.password == form.data['password']:
                    jobs = Job.objects.filter(company_id=company.company_id)
                    return render(request, 'company/company_dashboard.html', {'name': company.company_name, 'c_id': form.data['company_id'], 'jobs': jobs})
                else:
                    return HttpResponse("Wrong password")
            else:
                return HttpResponse("Wrong Login Id")
    else:
        form = LoginForm()

    return render(request, 'company/login.html', {'form': form})


@csrf_exempt
def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            c_id = form.data['email_id']
            new_company = Company.objects.create(company_name=form.data['company_name'], company_id=c_id, password=form.data['password'])
            new_company.save()
            print(c_id)
            return render_to_response('company/success.html', {'company_id': c_id})
    else:
        form = CompanyForm()

    return render(request, 'company/register_company.html', {'form': form})


@csrf_exempt
def register_for_job(request, c_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = JobForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(c_id+"#####")
            j_id= uuid.uuid1()
            new_job   = Job.objects.create(skills_required=form.data['skills_required'],
                                                       ctc=form.data['ctc'],
                                                       date_of_visit=form.data['date_of_visit'],
                                                       openings=form.data['openings'],
                                                       rounds=form.data['rounds'],
                                                       job_id=j_id,
                                                       company_id=c_id
                                                       )
            new_job.save()
            return HttpResponse('Successfully submitted job with id '+str(j_id))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = JobForm()

    return render(request, 'company/Job_register.html', {'form': form})


