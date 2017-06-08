from django import forms
from django.forms import ModelForm
from .models import JobProfile, CompanyUserProfile
from subjects import TECHNICAL_SKILL

class JobProfileForm(ModelForm):
    class Meta:
        model = JobProfile
        exclude = ['company', 'created_at']

    def __init__(self, *args, **kwargs):
        super(JobProfileForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'class' : "form-control"})
        #self.fields['department'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_type'].widget.attrs.update({'class' : "form-control", 'ng-model' : "job_type"})
        self.fields['job_description'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_location'].widget.attrs.update({'class' : "form-control"})
        self.fields['start_date'].widget.attrs.update({'class' : "form-control"})
        self.fields['salary_min'].widget.attrs.update({'class' : "form-control", 'ng-model':"salary_min"})
        self.fields['salary_max'].widget.attrs.update({'class' : "form-control", 'ng-model':"salary_max", 'ng-change':'validate_salary_max()'})
        self.fields['salary_type'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_period'].widget.attrs.update({'class' : "form-control"})
        self.fields['min_degree_qulification'].widget.attrs.update({'class' : "form-control"})

        self.fields['job_period_data'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_description'].widget.attrs['cols'] = 10
        self.fields['job_description'].widget.attrs['rows'] = 3
        self.fields['job_description'].widget.attrs['placeholder'] = 'Max. 300 characters'

        self.fields['sponsor_visa'].widget.attrs.update({'class' : "form-control"})
        self.fields['work_experience_year'].widget.attrs.update({'class' : "form-control"})
        #self.fields['work_experience_months'].widget.attrs.update({'class' : "form-control"})
        self.fields['industry_exp_year'].widget.attrs.update({'class' : "form-control"})
        #self.fields['industry_exp_months'].widget.attrs.update({'class' : "form-control"})
        self.fields['certifications'].widget.attrs.update({'class' : "form-control"})

        self.fields['tech_skills'].choices = [(str(options), str(options)) for options in TECHNICAL_SKILL]
        self.fields['tech_skills'].widget.attrs.update({'class' : "form-control js-basic-multiple", 'multiple':"multiple", 'width':"100%"})
    tech_skills = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control js-basic-multiple', 'style': 'width:100%'}),required=True)


class CompanyUserProfileForm(ModelForm):
    class Meta:
        model = CompanyUserProfile
        exclude = ['user_profile']

    def __init__(self, *args, **kwargs):
        super(CompanyUserProfileForm, self).__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs.update({'class' : "form-control"})
        self.fields['industry'].widget.attrs.update({'class' : "form-control"})
        self.fields['location'].widget.attrs.update({'class' : "form-control"})
        self.fields['company_size'].widget.attrs.update({'class' : "form-control"})
        self.fields['short_introduction'].widget.attrs.update({'class' : "form-control"})
        self.fields['founded_in'].widget.attrs.update({'class' : "form-control"})
        self.fields['vision'].widget.attrs.update({'class' : "form-control"})
        self.fields['mission'].widget.attrs.update({'class' : "form-control"})
        self.fields['long_description'].widget.attrs.update({'class' : "form-control"})
        self.fields['vision'].widget.attrs['cols'] = 10
        self.fields['vision'].widget.attrs['rows'] = 3
        self.fields['mission'].widget.attrs['cols'] = 10
        self.fields['mission'].widget.attrs['rows'] = 3
        self.fields['long_description'].widget.attrs['cols'] = 10
        self.fields['long_description'].widget.attrs['rows'] = 3
        self.fields['short_introduction'].widget.attrs['cols'] = 10
        self.fields['short_introduction'].widget.attrs['rows'] = 3
        
        self.fields['contact_details'].widget.attrs.update({'class' : "form-control"})
        self.fields['address'].widget.attrs.update({'class' : "form-control"})
        self.fields['address'].widget.attrs['cols'] = 10
        self.fields['address'].widget.attrs['rows'] = 3
        self.fields['contact_email'].widget.attrs.update({'class' : "form-control"})
        self.fields['phone_number'].widget.attrs.update({'class' : "form-control"})
        self.fields['website'].widget.attrs.update({'class' : "form-control"})
        self.fields['linkedIn'].widget.attrs.update({'class' : "form-control"})
        self.fields['facebook'].widget.attrs.update({'class' : "form-control"})
        self.fields['twitter'].widget.attrs.update({'class' : "form-control"})
        self.fields['logo'].widget.attrs.update({'class' : "form-control"})
        self.fields['banner'].widget.attrs.update({'class' : "form-control"})
