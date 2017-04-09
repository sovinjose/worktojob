import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from .models import CompanyUserProfile, JobProfile
from .form import JobProfileForm


class CompanyRegistration(View):

    def get(self, request):
        return render(request, 'company_registration.html')

    def post(self, request):
        try :
            request_data = json.loads(request.body)
            company_name = request_data.get("company_name")
            description = request_data.get("description")
            first_name = request_data.get("first_name")
            last_name = request_data.get("last_name")
            password = request_data.get("password")
            location = request_data.get("location")
            industry = request_data.get("industry")
            website = request_data.get("website")
            email = request_data.get("email")
            dictToSave = {
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
            }
            new_user = User.objects.create_user(
                username=email,password=password,
                **dictToSave
            )
            cmp_obj = CompanyUserProfile.objects.create(user_profile=new_user, company_name=company_name,
                                                        industry=industry, location=location, 
                                                        description=description, website=website)
            user = authenticate(username=new_user.username, password=password)
            status = False
            if user is not None:
                login(request, user)
                status = True
        except Exception as e:
            status = False
            print e.message
        context = {'status' : status}
        return HttpResponse(json.dumps(json.dumps(context)), content_type='application/json')


class CheckUsername(View):

    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
            status = True
        except ObjectDoesNotExist:
            status = False
        context = {
            'status' : status
        }
        return HttpResponse(json.dumps(context), content_type='application/json')


class CreateJobView(View):
    
    def get(self, request):
        form = JobProfileForm()
        context = {
            'form' : form
        }
        return render(request, 'create_job.html', context)

    def post(self, request):
        form = JobProfileForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.company = CompanyUserProfile.objects.get(user_profile=request.user)
            form_obj.save()
            return redirect('/job/%s/details' % (form_obj.id))
        context = {
                'form' : form
        }
        return render(request, 'create_job.html', context)

class ConfirmJobProfileView(View):

    def get(self, request, id):
        job_obj = JobProfile.objects.get(id=id)
        context = {
            'job_obj' : job_obj
        }
        return render(request, 'show_job_profile.html', context)


class UpdateJobView(UpdateView):
    form_class = JobProfileForm
    template_name = 'update_job.html'

    def get_object(self):
        return get_object_or_404(JobProfile, id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('confirm_job_profile', args=(self.object.pk,))


class JobListView(View):

    def get(self, request):
        job_list = JobProfile.objects.filter(company__user_profile=request.user)
        context = {
            'job_list' : job_list,
        }
        return render(request, 'job_list.html', context)







