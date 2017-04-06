import json
from django.shortcuts import render, HttpResponse
from django.contrib.auth import authenticate, login
from django.views import View
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import CompanyUserProfile


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