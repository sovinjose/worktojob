import json
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.views.generic import UpdateView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms.models import model_to_dict

from .forms import UserProfileForm, CompanyProfileForm, OpeningDetailsForm, UpdateCompanyProfileForm, CreateCompanyProfileForm
from. models import CompanyProfile, OpeningDetails


class HomeView(View):

    def get(self, requests):
        return HttpResponseRedirect('/company/details')


class GetUserProfileView(View):
    def get(self, requests):
        context = {
            'cmpny_form' : CompanyProfileForm()
        }
        return render(requests, 'create_user_profile.html', context)


class CreateUserProfileView(View):
    def post(self, requests):
        cmpny_form = CompanyProfileForm(json.loads(requests.body))
        if cmpny_form.is_valid():
            form_obj = cmpny_form.save(commit=False)
            form_obj.user_profile=requests.user
            form_obj.save()
            status = True
        else:
            status = False
        context = {'status' : status}
        return HttpResponse(json.dumps(context), content_type='application/json')


class UpdateUserProfileView(View):
    def post(self, requests):
        d_obj = json.loads(requests.body)
        form = CompanyProfileForm(d_obj)
        if form.is_valid():
            CompanyProfile.objects.filter(user_profile=requests.user).update(**d_obj)
            status = True
        else:
            status = False
        context = {'status' : status}
        return HttpResponse(json.dumps(context), content_type='application/json')


class SaveUserProfileView(UpdateView):
    form_class = UpdateCompanyProfileForm
    success_url = '/'

    def get_object(self, queryset=None):
        obj, created = CompanyProfile.objects.get_or_create(user_profile=self.request.user)
        return obj


class CreateJobProfileView(View):

    def get(self, requests):
        context = {
            'job_details_form' : OpeningDetailsForm()
        }
        return render(requests, 'create_job_profile.html', context)


class CreateCompanyAccount(View):

    def get(self, requests):
        cmpny_form = CreateCompanyProfileForm()
        context = {
            'cmpny_form' : cmpny_form
        }
        return render(requests, 'user_registration.html', context)

    def post(self, requests):
        email = requests.POST.get('email', None)
        password = requests.POST.get('password', None)
        password2 = requests.POST.get('password2', None)
        #try:
        if email and password:
            #cmpny_form = CompanyProfileForm(requests.POST)
            #if cmpny_form.is_valid():
            user = User.objects.create_user(
                                username=email,
                                password=password,
                                first_name=requests.POST.get('first_name'),
                                last_name=requests.POST.get('last_name'),
                                email=email
                            )
                #cmp_frm = cmpny_form.save(commit=False)
                #cmp_frm.user_profile = user
                #cmp_frm.save()
            messages.add_message(requests, messages.INFO, 'successfully crested the user')
            user = authenticate(username=email, password=password)
            login(requests, user)
            return HttpResponseRedirect('/home')
        else:
            messages.add_message(requests, messages.ERROR, 'Please enter Email And Apssword.')
        #except Exception as e:
        #    messages.add_message(requests, messages.ERROR, e.message)
        context = {
            'cmpny_form' : CreateCompanyProfileForm(requests.POST)
        }
        return render(requests, 'user_registration.html', context)


class CompanyAccountDetails(View):

    def get(self, requests):
        #cmp_obj = CompanyProfile.objects.get(user_profile=requests.user)
        cmp_obj = OpeningDetails.objects.filter(company__user_profile = requests.user)
        context = {
            'cmp_obj' : cmp_obj,
            #'openong_details' : openong_details
        }
        return render(requests, 'job_profile_details.html', context)


class PostNewJob(View):

    def get(self, requests):
        form = OpeningDetailsForm()
        context = {
            'form' : form
        }
        return render(requests, 'post_job.html', context)

    def post(self, requests):
        form = OpeningDetailsForm(requests.POST)
        if form.is_valid():
            cmp_obj = CompanyProfile.objects.get(user_profile=requests.user)
            form_obj = form.save(commit=False)
            form_obj.company = cmp_obj
            form_obj.save()
            return HttpResponseRedirect('/jobProfile/%s/details' % (form_obj.id))
        else:
            print form.errors
            context = {
                'form' : form
            }
        return render(requests, 'post_job.html', context)


class CompleteJobProfile(View):

    def get(self, requests, pk):
        context = {
            'job_id' : pk
        }
        return render(requests, 'post_job_details.html', context)

    def post(self, requests, pk):
        job_profile = requests.POST.get('job_profile')
        opening_details = OpeningDetails.objects.get(id=pk)
        opening_details.job_profile = job_profile
        opening_details.save()
        return HttpResponseRedirect('/company/details')



class JobDetails(View):

    def get(self, requests, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        context = {
            'opng_details' : opng_details
        }
        return render(requests, 'job_details.html', context)


class CloseJobStatus(View):

    def post(self, requests, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        opng_details.active_status = False
        opng_details.save()
        return HttpResponseRedirect('/')


class CompanyJobListView(View):

    def get(self, requests):
        cmp_details = CompanyProfile.objects.get(user_profile=requests.user)
        opng_details = OpeningDetails.objects.all()
        context = {
            'opng_details' : opng_details,
            'cmp_details' : cmp_details
        }
        return render(requests, 'company_job_list.html', context)



