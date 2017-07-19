from django.conf.urls import url
from. views import ( CompanyRegistration, CheckUsername, 
					CreateJobView, ConfirmJobProfileView, 
					UpdateJobView, JobListView, JobMatchingList, ProfileSettings,
					CompanySettings, AccountSettings, ChangeLoginEmail, GetSubjectOptionList, GetEmployeDetailsView)

urlpatterns = [

	url(r'^$', JobListView.as_view(), name='company_job_list'),
	url(r'register$', CompanyRegistration.as_view(), name='company_registration_template'),
	url(r'create/company/profile$', CompanyRegistration.as_view(), name='create_company_profile'),
	url(r'check/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/availability$', CheckUsername.as_view(), name='company_registration_template'),
	url(r'create/job$', CreateJobView.as_view(), name='create_job'),
	url(r'job/(?P<id>[0-9]+)/details$', ConfirmJobProfileView.as_view(), name='confirm_job_profile'),
	url(r'update/(?P<pk>[0-9]+)/job$', UpdateJobView.as_view(), name='update_job_profile'),
	url(r'matching/(?P<job_id>[0-9]+)/list$', JobMatchingList.as_view(), name='job_matching_list'),

	url(r'profile/settings$', ProfileSettings.as_view(), name='user_profile_settings'),
	url(r'company/(?P<pk>[0-9]+)/settings$', CompanySettings.as_view(), name='company_profile_settings'),
	url(r'myaccount$', AccountSettings.as_view(), name='my_account_settings'),
	url(r'change/email$', ChangeLoginEmail.as_view(), name='change_login_email'),


	url(r'get/(?P<subject_val>[0-9]+)/value$', GetSubjectOptionList.as_view(), name='get_subject_value'),

	url(r'get/(?P<id>[0-9]+)/candidate$', GetEmployeDetailsView.as_view(), name='get_emp_details'),








]