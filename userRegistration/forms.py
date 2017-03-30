import re
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from .models import UserProfile, CompanyProfile, OpeningDetails


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']


class CreateCompanyProfileForm(ModelForm):

    class Meta:
        model = CompanyProfile
        fields = ['last_name', 'first_name', 'email']

    def __init__(self, *args, **kwargs):
        super(CreateCompanyProfileForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.last_name"})
        self.fields['first_name'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.first_name"})
        self.fields['email'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.email"})




class UpdateCompanyProfileForm(ModelForm):
    class Meta:
        model = CompanyProfile
        fields = ('description', 'website', 'linkdin_page', 'facebook_page', 'logo')



class CompanyProfileForm(ModelForm):

    class Meta:
        model = CompanyProfile
        exclude = ['user_profile']

    def __init__(self, *args, **kwargs):
        super(CompanyProfileForm, self).__init__(*args, **kwargs)
        self.fields['last_name'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.last_name"})
        self.fields['first_name'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.first_name"})
        self.fields['email'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.email"})
        self.fields['job_title'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.job_title"})
        self.fields['phone_number'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.phone_number"})
        self.fields['company_name'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.company_name"})
        self.fields['industry'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.industry"})
        self.fields['company_size'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.company_size"})
        self.fields['address'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.address"})
        self.fields['description'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.description"})
        self.fields['website'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.website"})
        self.fields['linkdin_page'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.linkdin_page"})
        self.fields['facebook_page'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.facebook_page"})
        self.fields['logo'].widget.attrs.update({'class' : "form-control", "ng-model":"formData.logo"})


    def clean_first_name(self):
        if re.match(r"^([a-zA-Z._ ]*)$", self.cleaned_data['first_name'].strip()):
            return self.cleaned_data['first_name'].strip()
            if len(self.cleaned_data['first_name']) > 30:
                raise forms.ValidationError('Name seems to be too long')
        raise forms.ValidationError('Please enter a valid  name')

    def clean_name(self):
        if re.match(r"^([a-zA-Z._ ]*)$", self.cleaned_data['name'].strip()):
            return self.cleaned_data['name'].strip()
            if len(self.cleaned_data['name']) > 20:
                raise forms.ValidationError('Name seems to be too long')
        raise forms.ValidationError('Please enter a valid  company name')

    def clean_contact_number(self):
        if re.match(r"^([0-9+(). -]{6,15})$", self.cleaned_data['contact_number']):
            if len(self.cleaned_data['contact_number']) < 6:
                raise forms.ValidationError('Phone Number must contain at least six digits')
            return self.cleaned_data['contact_number'].strip()
        raise forms.ValidationError('Invalid Contact No.')


    # def clean_email(self):
    #     try:
    #         user = User.objects.get(
    #             username=self.cleaned_data['email']
    #         )
    #     except ObjectDoesNotExist:
    #             return self.cleaned_data['email']
    #     raise forms.ValidationError('This e-mail ID already exists.')


class OpeningDetailsForm(ModelForm):

    class Meta:
        model = OpeningDetails
        exclude = ['company', 'created_at']

    def __init__(self, *args, **kwargs):
        super(OpeningDetailsForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'class' : "form-control"})
        self.fields['department'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_type'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_description'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_location'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_start_date'].widget.attrs.update({'class' : "form-control"})
        #self.fields['job_end_date'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_profile'].widget.attrs.update({'class' : "form-control"})
        self.fields['salary_min'].widget.attrs.update({'class' : "form-control"})
        self.fields['salary_max'].widget.attrs.update({'class' : "form-control"})

        self.fields['job_description'].widget.attrs['cols'] = 10
        self.fields['job_description'].widget.attrs['rows'] = 5
        self.fields['job_description'].widget.attrs['placeholder'] = 'Max. 300 characters'

        self.fields['job_profile'].widget.attrs['cols'] = 10
        self.fields['job_profile'].widget.attrs['rows'] = 15

        #self.fields['Keywords'].widget.attrs.update({'class' : "form-control"})
        # self.fields['number_of_vacancies'].widget.attrs.update({'class' : "form-control"})
        # self.fields['location'].widget.attrs.update({'class' : "form-control"})
        # self.fields['industry'].widget.attrs.update({'class' : "form-control"})
        # self.fields['functional_area'].widget.attrs.update({'class' : "form-control"})
        # self.fields['job_role'].widget.attrs.update({'class' : "form-control"})
        # self.fields['qualifications'].widget.attrs.update({'class' : "form-control"})
        # self.fields['contact_number'].widget.attrs.update({'class' : "form-control"})
        # self.fields['contact_email'].widget.attrs.update({'class' : "form-control"})
