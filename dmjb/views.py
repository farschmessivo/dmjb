from django.shortcuts import render, redirect
from django.http import HttpResponse
from dmjb.models import Job
from dmjb.forms import JobForm
from django.core.mail import send_mail
from django.contrib import messages


# def index(request):
#     return HttpResponse("Dmjb 4 lyf!")

# Create your views here.


def index(request):
    # Construct a dictionary to pass to the template engine as its context.

    jobs_list = Job.objects.order_by('-views')
    context_dict = {'jobs': jobs_list}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'dmjb/index.html', context=context_dict)


def show_job(request, job_slug):
    context_dict = {}

    try:
        job = Job.objects.get(slug=job_slug)
        context_dict['job'] = job

    except Job.DoesNotExist:
        context_dict['job'] = None

    return render(request, 'dmjb/job.html', context=context_dict)


def add_job(request):
    form = JobForm()

    if request.method == 'POST':
        form = JobForm(request.POST)

        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved
            # We could give a confirmation message
            # But since the most recent category added is on the index page
            #  Then we can direct the user back to the index page.
            return index(request)
        else:
            print(form.errors)
            # return redirect({'add_job': form})

    return render(request, 'dmjb/add_job.html', {'form': form})