"""WorkToJob URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from views import ( HomeView, CreateUserProfileView, CreateCompanyAccount, 
								CompanyAccountDetails, PostNewJob, JobDetails, CloseJobStatus,
								CompanyJobListView, GetUserProfileView, UpdateUserProfileView, 
								SaveUserProfileView, CreateJobProfileView)

urlpatterns = [

	url(r'^$', HomeView.as_view(), name='home'),
	url(r'^company/registration/$', CreateCompanyAccount.as_view(), name='register_company_profile'),
	url(r'^company/details$', CompanyAccountDetails.as_view(), name='company_details'),
	url(r'^create/new/job$', PostNewJob.as_view(), name='create_new_job'),
	url(r'^job/(?P<pk>[0-9]+)/details$', JobDetails.as_view(), name='job_details'),
	url(r'^close/(?P<pk>[0-9]+)/job$', CloseJobStatus.as_view(), name='close_the_position'),
	url(r'^company/job/list$', CompanyJobListView.as_view(), name='company_job_list_view'),

	url(r'^home$', GetUserProfileView.as_view(), name='GetUserProfileView'),

	url(r'^create/user/profile$', CreateUserProfileView.as_view(), name='CreateUserProfileView'),
	url(r'^update/user/profile$', UpdateUserProfileView.as_view(), name='UpdateUserProfileView'),
	url(r'^save/profile$', csrf_exempt(SaveUserProfileView.as_view()), name='SaveUserProfileView'),
	url(r'^create/job/profile$', CreateJobProfileView.as_view(), name='create_job_profile'),





]
