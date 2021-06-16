from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.core.serializers import serialize
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from profiles.forms import *
from profiles.models import *
from profiles.permission import *
import datetime

User = get_user_model()



def index(request):

    published_jobs = Job.objects.filter(is_published=True).order_by('-timestamp')
    
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    
    
    #paginator = Paginator(jobs, 3)
    #page_number = request.GET.get('page',None)
    #page_obj = paginator.get_page(page_number)

    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_jobs = Job.objects.all().count()
    num_companies = Company.objects.all().count()
    num_jobseekers = JobSeeker.objects.all().count()

    # Available jobs (status = 'a')
    num_jobs_available = Job.objects.filter(status__exact='a').count()


    context = {
        'num_jobs': num_jobs,
        'num_companies': num_companies,
        'num_jobseekers': num_jobseekers,
        'num_published_jobs' : published_jobs.count(),
        'num_jobs_available': num_jobs_available,
        'num_visits': num_visits,
    }

    # Render the HTML template home.html with the data in the context variable
    return render(request, 'index.html', context=context)

from django.views import generic    
    
class JobListView(generic.ListView):
    model = Job
    paginate_by = 10
    #context_object_name = 'job_list'   
    #queryset = Job.objects.filter(is_published=True,is_closed=False)[:5] # Get 5 Jobs published but not closed
    #template_name = 'profiles/job_list.html'  # template name/location

class JobDetailView(generic.DetailView):
    model = Job

class CompanyListView(generic.ListView):
    model = Company
    paginate_by = 10
    

class CompanyDetailView(generic.DetailView):
    model = Company



def create_job_View(request,pk):
    company = get_object_or_404(Company, pk=pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = JobForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            job = Job()
            # process the data in form.cleaned_data as required 
            
            #Add company and job_type (change experience required)
            
            job.designation = form.cleaned_data['designation']
            job.location = form.cleaned_data['location']
            job.job_description = form.cleaned_data['job_description']
            job.exp_required=form.cleaned_data['exp_required']
            job.salary=form.cleaned_data['salary']
            job.job_type=form.cleaned_data['job_type']
            #job.job_type='FT'
            job.is_published=True
            job.date_loggedin=datetime.date.today()
            job.last_date=form.cleaned_data['last_date']
            job.company=company
            job.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("profiles:single-job", kwargs={'pk': job.id})) 
            #redirect(reverse("profiles:single-job", kwargs={'pk': job.id}))
                                   

    # If this is a GET (or any other method) create the default form.
    else:
        form = JobForm()

    context = {
        'form': form,
        
    }

    return render(request, 'profiles/post-job.html', context)      


def create_profile_View(request,pk):
    
    user = get_object_or_404(User, pk=pk)
    
    fullname = user.get_full_name().split()
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = JobSeekerForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            jobSeeker = JobSeeker()
            # process the data in form.cleaned_data as required 
            
            #Add company and job_type (change experience required)
            jobSeeker.fname = form.cleaned_data['fname']
            jobSeeker.mname = form.cleaned_data['mname']
            jobSeeker.lname = form.cleaned_data['lname']
            jobSeeker.gender= form.cleaned_data['gender']
            jobSeeker.address=form.cleaned_data['address']
            #jobSeeker.country =form.cleaned_data['country']
            #jobSeeker.skill =form.cleaned_data['skill']
            #jobSeeker.education =form.cleaned_data['education']
            jobSeeker.email=form.cleaned_data['email']
            jobSeeker.mobile=form.cleaned_data['mobile']
            jobSeeker.experience = form.cleaned_data['experience']
            jobSeeker.date_registration=datetime.date.today()
            #jobSeeker.status='Visiting'
            
            jobSeeker.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("login")) 
            #return HttpResponseRedirect(reverse("profiles:user-detail")) 
           
                                   
    # If this is a GET (or any other method) create the default form.
    else:
       
        form = JobSeekerForm(initial={'fname': user.get_short_name(),'email': str(user),'lname':fullname[1]})

    context = {
        'form': form,
    
    }


    return render(request, 'profiles/user_detail.html', context) 





class JobSeekerCreate(CreateView):
    model = JobSeeker
    fields = ['fname', 'lame', 'gender', 'address','email','mobile','experience','education','skills']
    #template_name = 'jobseeker_form.html'
    #form_class = ContactForm
    
    
   
   # def form_valid(self, form):
      #  success_url = 'profiles/index.html'
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #fields = ['fname', 'lname', 'gender', 'address','email','mobile','experience','education','skills']
     #   username =self.request.user.get_username
      #  print("****** User******" + str(user))
        #user = get_object_or_404(User, id=id)
        #initial = {'fname': user.get_short_name(),'email': user.get_email_field_name()}
      #  return super().form_valid(form)
    

class JobSeekerUpdate(UpdateView):
    #user = get_object_or_404(User, pk=pk)
    model = JobSeeker
    fields = ['address','mobile','experience','education','skills']

class JobSeekerDelete(DeleteView):
    model = JobSeeker
    success_url = reverse_lazy('profiles:index')


def create_company_View(request,pk):
    
    user = get_object_or_404(User, pk=pk)
    
    fullname = user.get_full_name().split()
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = CompanyForm(request.POST)

        # Check if the form is valid:
        if form.is_valid():
            company = Company()
            # process the data in form.cleaned_data as required 
            
            #Add company and job_type (change experience required)
            company.cname = form.cleaned_data['cname']
            company.cdescription = form.cleaned_data['cdescription']
            company.contact = form.cleaned_data['contact']
            company.caddress=form.cleaned_data['caddress']
            #company.country =form.cleaned_data['country']
            
            company.email=form.cleaned_data['email']
            company.mobile=form.cleaned_data['mobile']
            
            company.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect(reverse("login")) 
            #return HttpResponseRedirect(reverse("profiles:user-detail")) 
           
                                   
    # If this is a GET (or any other method) create the default form.
    else:
        
        form = CompanyForm(initial={'cname': user.get_short_name(),'email': str(user)})

    context = {
        'form': form,
    
    }


    return render(request, 'profiles/user_detail.html', context) 

#applying for Job
@login_required(login_url=reverse_lazy('login'))
def apply_job_View(request,id):
    

    user = get_object_or_404(User, id=request.user.id)
    
    jobSeeker = JobSeeker.objects.get(email__exact=str(user))
    
    job = get_object_or_404(Job, id=id)
    applicant = JobApplicant.objects.filter(jobSeeker=jobSeeker,job=job)
   
    

    if not applicant:
        if request.method == 'POST':
            form = JobApplicantForm(request.POST)
            if form.is_valid():
                jobApplicant = JobApplicant()
                jobApplicant.job = job
                jobApplicant.jobSeeker = jobSeeker
                jobApplicant.save()

                print('You have successfully applied for this job!')
                return redirect(reverse("profiles:jobs"))

        else:
            form = JobApplicantForm(initial={'job': job})

        context = {
        'form': form,
        
        }

        return render(request, 'profiles/apply-job.html', context)   

    else:

        print('You already applied for the Job!')

        return redirect(reverse("profiles:jobs"))
        

#User can search job with multiple fields
def search_result_view(request):
   
    job_list = Job.objects.order_by('-timestamp')

    # Keywords
    if 'job_designation' in request.GET:
        job_designation = request.GET['job_designation']

        if job_designation:
            job_list = job_list.filter(designation__icontains=job_designation)

    # location
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            job_list = job_list.filter(location__icontains=location)

    # Job Type
    if 'job_type' in request.GET:
        job_type = request.GET['job_type']
        if job_type:
            job_list = job_list.filter(job_type__iexact=job_type)
  
    context = {

        'job_list': job_list,

    }
    return render(request, 'profiles/result.html', context)


def find_job_view(request):
     context = {

        'request': request,

    }
     return render(request, 'profiles/find_job.html', context)
    #return redirect(reverse("profiles:find_job"))