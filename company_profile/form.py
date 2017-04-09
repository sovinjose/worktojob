from django import forms
from django.forms import ModelForm
from .models import JobProfile

class JobProfileForm(ModelForm):
    class Meta:
        model = JobProfile
        exclude = ['company', 'created_at']

    def __init__(self, *args, **kwargs):
        super(JobProfileForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'class' : "form-control"})
        self.fields['department'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_type'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_description'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_location'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_start_date'].widget.attrs.update({'class' : "form-control"})
        self.fields['salary_min'].widget.attrs.update({'class' : "form-control"})
        self.fields['salary_max'].widget.attrs.update({'class' : "form-control"})
        self.fields['job_description'].widget.attrs['cols'] = 10
        self.fields['job_description'].widget.attrs['rows'] = 3
        self.fields['job_description'].widget.attrs['placeholder'] = 'Max. 300 characters'