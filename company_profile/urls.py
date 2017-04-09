from django.conf.urls import url
from. views import ( CompanyRegistration, CheckUsername, 
					CreateJobView, ConfirmJobProfileView, 
					UpdateJobView, JobListView)

urlpatterns = [

	url(r'^$', JobListView.as_view(), name='company_job_list'),
	url(r'register$', CompanyRegistration.as_view(), name='company_registration_template'),
	url(r'create/company/profile$', CompanyRegistration.as_view(), name='create_company_profile'),
	url(r'check/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/availability$', CheckUsername.as_view(), name='company_registration_template'),
	url(r'create/job$', CreateJobView.as_view(), name='create_job'),
	url(r'job/(?P<id>[0-9]+)/details$', ConfirmJobProfileView.as_view(), name='confirm_job_profile'),
	url(r'update/(?P<pk>[0-9]+)/job$', UpdateJobView.as_view(), name='update_job_profile'),



]