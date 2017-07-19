import json
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login
from django.views import View
from django.views.generic import UpdateView
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash

from .models import CompanyUserProfile, JobProfile, Employe, UserProfile, TechSkill
from .form import JobProfileForm, CompanyUserProfileForm
from django.contrib.auth.forms import PasswordChangeForm

from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


from subjects import SUBJECT_TUPLE

class CompanyRegistration(View):

    def get(self, request):
        return render(request, 'company_registration.html')

    def post(self, request):
        try :
            request_data = json.loads(request.body)
            print request_data
            email = request_data.get("email")
            password = request_data.get("password")
            first_name = request_data.get("first_name")
            last_name = request_data.get("last_name")
            
            company_name = request_data.get("company_name", None)
            industry = request_data.get("industry", None)
            company_size = request_data.get("company_size",None)
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
                                                        industry=industry, company_size=company_size, 
                                                        )
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


class CreateJobView(View):
    
    def get(self, request):
        form = JobProfileForm()
        context = {
            'form' : form
        }
        return render(request, 'create_job.html', context)

    def post(self, request):
        form = JobProfileForm(request.POST)
        if form.is_valid():
            form_obj = form.save(commit=False)
            form_obj.company = CompanyUserProfile.objects.get(user_profile=request.user)
            form_obj.save()
            skill_list = [ TechSkill(text=obj, job_profile=form_obj) for  obj in request.POST.getlist('tech_skills')]
            if skill_list:
                TechSkill.objects.bulk_create(skill_list)
            return redirect('/job/%s/details' % (form_obj.id))
        print form.errors
        context = {
                'form' : form
        }
        return render(request, 'create_job.html', context)

class ConfirmJobProfileView(View):

    def get(self, request, id):
        job_obj = JobProfile.objects.get(id=id)
        skill = TechSkill.objects.filter(job_profile=id)
        context = {
            'job_obj' : job_obj,
            'skill' : skill
        }
        return render(request, 'show_job_profile.html', context)


class UpdateJobView(UpdateView):
    form_class = JobProfileForm
    template_name = 'update_job.html'

    def get_object(self):
        return get_object_or_404(JobProfile, id=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('confirm_job_profile', args=(self.object.pk,))


    def get_context_data(self, **kwargs):
        context = super(UpdateJobView, self).get_context_data(**kwargs)
        tech_list = TechSkill.objects.filter(job_profile=self.kwargs['pk']).values('text')
        print ">>>>>>>>>>>>>>>>>>>", tech_list
        context['skill_sets'] = list(tech_list)
        return context


class JobListView(View):

    def get(self, request):
        job_list = JobProfile.objects.filter(company__user_profile=request.user)
        context = {
            'job_list' : job_list,
        }
        return render(request, 'job_list.html', context)

class JobMatchingList(View):

    def get(self, request, job_id):
        emp_obj = Employe.objects.all()
        job_obj = JobProfile.objects.get(id=job_id)

        context = {
            'emp_obj' : emp_obj,
            'job_obj' :job_obj
        }
        return render(request, 'job_matching_list.html', context)

class ProfileSettings(View):

    def get(self, request):
        profile_obj = UserProfile.objects.filter(user=request.user).first()
        context = {
            'profile_obj' : profile_obj
        }
        return render(request, 'profile_settings.html', context)

    def post(self, request): 
        mob_number =  request.POST['mob_number']
        city =  request.POST.get('city')
        print city
        logo =  request.FILES.get('profile_pic')
        user_obj = User.objects.get(id=request.user.id)
        user_obj.first_name = request.POST['first_name']
        user_obj.last_name = request.POST['last_name']
        user_obj.save()
        profile_obj, created = UserProfile.objects.get_or_create(user=request.user, 
                            defaults={"mob_number": mob_number, "city": city, "logo": logo,}
                            )
        if created:
            pass
        else:
            profile_obj.mob_number = mob_number
            profile_obj.city = city
            if logo:
                profile_obj.logo = logo
            profile_obj.save()
        return redirect('/profile/settings')


class CompanySettings(UpdateView):
    form_class = CompanyUserProfileForm
    template_name = 'company_settings.html'

    def get_object(self):
        return get_object_or_404(CompanyUserProfile, user_profile=self.kwargs['pk'])

    def get_success_url(self):
        return reverse('company_profile_settings', args=(self.kwargs['pk'],))


class AccountSettings(View):

    def get(self, request):
        form = PasswordChangeForm(request.user)
        context = {
            'form' : form
        }
        return render(request, 'account_settings.html', context)

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        old_pass = request.POST['old_password']
        new_password1 = request.POST['new_password1']
        new_password2 = request.POST['new_password2']
        usr_obj = User.objects.get(id=request.user.id)
        user_auth = usr_obj.check_password(old_pass)
        if not user_auth:
            messages.error(request, 'Please enter correct Password.')
            return render(request, 'account_settings.html')
        if new_password1 == new_password2 and len(new_password1)>2:
            request.user.set_password(new_password1)
            update_session_auth_hash(request, request.user)
            request.user.save(update_fields=['password'])
            messages.success(request, 'Your password was successfully updated!')
        else:
            messages.error(request, 'Password does not match the confirm password. // password not valid')

        return render(request, 'account_settings.html')


class ChangeLoginEmail(View):

    def get(self, request):
        form = PasswordChangeForm(request.user)
        context = {
            'form' : form,
            'email_error' :True
        }
        return render(request, 'account_settings.html', context)

    def post(self, request):
        new_email = request.POST['new_email']
        usr_obj = User.objects.get(id=request.user.id)
        if new_email:
            try:
                mail = User.objects.get(username=new_email)
                messages.error(request, 'email already exists.')
                return redirect('/change/email')
            except:
                usr_obj.username = new_email
                usr_obj.email = new_email
                usr_obj.save()
                messages.success(request, 'Your email was successfully updated!')
        else:
            messages.error(request, 'Please enter correct Email.')

        return redirect('/change/email')


class GetSubjectOptionList(View):

    def get(self, request, subject_val):
        print "????????????????????", subject_val
        print SUBJECT_TUPLE[subject_val]
        return HttpResponse(json.dumps(SUBJECT_TUPLE[subject_val]), content_type="application/json")


class GetEmployeDetailsView(View):

    def get(self, request, id):
        emp = Employe.objects.get(id=id)
        d = {

            'name' : emp.name,
            'department' : emp.department,
            'college' : emp.college,
            'degree' : emp.degree,
            'score' : emp.score,
            'location' : emp.location,
            'id' : emp.id,
            'status' : emp.status

        }
        return HttpResponse(json.dumps(d), content_type="application/json")




class DwonloadCandidatePDF(View):
    
    def get(self, request):
        # Create the HttpResponse object with the appropriate PDF headers.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="candidate_details.pdf"'

        buffer = BytesIO()
        
        # Create the PDF object, using the BytesIO object as its "file."
        p = canvas.Canvas(buffer)
        n = 100

        if request.GET.get('val_id', None):
            ob = Employe.objects.get(id=request.GET.get('val_id'))
            p.drawString(10, n, ob.name)
            n=n+10
            p.drawString(10, n, ob.department)
            n=n+10
            p.drawString(10, n, ob.college)
            n=n+10
            p.drawString(10, n, ob.degree)
            n=n+10
            p.drawString(10, n, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>%s Details<<<<<<<<<<<<<<<<<<<<<<<<<<<' % ob.name)
            n=n+10
        else:
            emp = Employe.objects.all()[:4]
            for ob in emp:

                # Draw things on the PDF. Here's where the PDF generation happens.
                # See the ReportLab documentation for the full list of functionality.
                p.drawString(10, n, ob.name)
                n=n+10
                p.drawString(10, n, ob.department)
                n=n+10
                p.drawString(10, n, ob.college)
                n=n+10
                p.drawString(10, n, ob.degree)
                n=n+10
                p.drawString(10, n, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>%s Details<<<<<<<<<<<<<<<<<<<<<<<<<<<' % ob.name)
                n=n+10

        # Close the PDF object cleanly.
        p.showPage()
        p.save()

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        response.write(pdf)
        return response

class SendInvitationRequest(View):

    def get(self, request):
        lis = request.GET.getlist('lis')
        for i in lis:
            ob = Employe.objects.get(id=i)
            ob.status = 'send invitation'
            ob.save()
        return HttpResponse(json.dumps({'status': True}), content_type="application/json")








