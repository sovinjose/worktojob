from django.conf.urls import url
from. views import CompanyRegistration, CheckUsername

urlpatterns = [

	url(r'^$', CompanyRegistration.as_view(), name='company_registration_template'),
	url(r'create/company/profile$', CompanyRegistration.as_view(), name='create_company_profile'),
	url(r'check/(?P<username>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/availability$', CheckUsername.as_view(), name='company_registration_template'),


]