import json
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib import messages
from django.views.generic import UpdateView

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import get_list_or_404, get_object_or_404
from django.forms.models import model_to_dict

from .forms import (UserProfileForm, CompanyProfileForm, OpeningDetailsForm, 
                            UpdateCompanyProfileForm, UserForm)
from. models import CompanyProfile, OpeningDetails


class HomeView(View):

    def get(self, request):
        return HttpResponseRedirect('/company/details')


class GetUserProfileView(View):
    def get(self, request):
        context = {
            'cmpny_form' : CompanyProfileForm()
        }
        return render(request, 'create_user_profile.html', context)


class CreateUserProfileView(View):
    def post(self, request):
        cmpny_form = CompanyProfileForm(json.loads(request.body))
        if cmpny_form.is_valid():
            form_obj = cmpny_form.save(commit=False)
            form_obj.user_profile=request.user
            form_obj.save()
            status = True
        else:
            status = False
        context = {'status' : status}
        return HttpResponse(json.dumps(context), content_type='application/json')


class UpdateUserProfileView(View):
    def post(self, request):
        d_obj = json.loads(request.body)
        form = CompanyProfileForm(d_obj)
        if form.is_valid():
            CompanyProfile.objects.filter(user_profile=request.user).update(**d_obj)
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

    def get(self, request):
        context = {
            'job_details_form' : OpeningDetailsForm()
        }
        return render(request, 'create_job_profile.html', context)


class CreateCompanyAccount(View):

    def get(self, request):
        form = UserForm()
        context = {
            'form' : form
        }
        return render(request, 'user_registration.html', context)

    def post(self, request):        
        form = UserForm(request.POST)
        if form.is_valid():
            password = request.POST['password']
            dictToSave = {
                'email': form.cleaned_data['email'],
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name']
            }
            new_user = User.objects.create_user(
                username=form.cleaned_data['email'],password=password,
                **dictToSave
            )
            user = authenticate(username=new_user.username, password=password)
            if user is not None:
                login(request, user)
            return HttpResponseRedirect('/home')
        else:
            context = {
                'form' : UserForm(request.POST)
            }
            return render(request, 'user_registration.html', context)


class CompanyAccountDetails(View):

    def get(self, request):
        #cmp_obj = CompanyProfile.objects.get(user_profile=request.user)
        cmp_obj = OpeningDetails.objects.filter(company__user_profile = request.user)
        context = {
            'cmp_obj' : cmp_obj,
            #'openong_details' : openong_details
        }
        return render(request, 'job_profile_details.html', context)


class PostNewJob(View):

    def get(self, request):
        form = OpeningDetailsForm()
        context = {
            'job_details_form' : form
        }
        return render(request, 'create_job_profile.html', context)

    def post(self, request):
        form = OpeningDetailsForm(request.POST)
        if form.is_valid():
            cmp_obj = CompanyProfile.objects.get(user_profile=request.user)
            form_obj = form.save(commit=False)
            form_obj.company = cmp_obj
            form_obj.save()
            return HttpResponseRedirect('/jobProfile/%s/details' % (form_obj.id))
        else:
            print form.errors
            context = {
                'job_details_form' : form
            }
        return render(request, 'create_job_profile.html', context)


class CompleteJobProfile(View):

    def get(self, request, pk):
        context = {
            'job_id' : pk
        }
        return render(request, 'post_job_details.html', context)

    def post(self, request, pk):
        job_profile = request.POST.get('job_profile')
        opening_details = OpeningDetails.objects.get(id=pk)
        opening_details.job_profile = job_profile
        opening_details.save()
        return HttpResponseRedirect('/company/details')




class EmployeJobDetails(View):

    def get(self, request, pk):
        opening_details = OpeningDetails.objects.get(id=pk)
        context = {
            'opening_details': opening_details
        }
        return render(request, 'employee_list.html', context)






class JobDetails(View):

    def get(self, request, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        context = {
            'opng_details' : opng_details
        }
        return render(request, 'job_details.html', context)


class CloseJobStatus(View):

    def post(self, request, pk):
        opng_details = OpeningDetails.objects.get(id=pk)
        opng_details.active_status = False
        opng_details.save()
        return HttpResponseRedirect('/')


class CompanyJobListView(View):

    def get(self, request):
        job_list = OpeningDetails.objects.filter(company__user_profile=request.user)
        context = {
            'job_list' : job_list,
        }
        return render(request, 'job_list.html', context)



