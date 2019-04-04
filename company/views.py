from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NameForm

names = []

@csrf_exempt
def submit(request):
    context = {}
    request_context = RequestContext(request)
    return render_to_response('company/success.html', context,  request_context)


@csrf_exempt
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            names.append(form.data['company_name'])
            names.append(form.data['skills_required'])
            names.append(form.data['ctc'])

            return HttpResponseRedirect('thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'company/login.html', {'form': form})


@csrf_exempt
def thanks(request):
    context_dict = {}
    context_dict = {'names': names}
    print(context_dict)
    return render_to_response('company/success.html', context_dict)
