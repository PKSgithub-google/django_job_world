from django.db import models
from datetime import date


GENDER = (
    ('M', "Male"),
    ('F', "Female"),

)

STATUS = (
    ('A', "Applied"),
    ('V', "Visting"),
    ('C', "Confirm"),
    ('R', "Rejected"),
)

EXP_YEARS = (
    ('1', "1 year"),
    ('2', "2 years"),
    ('3', "3 years"),
    ('4', "4 years"),
    ('5', "5 year"),
    ('6', "6 years"),
    ('7', "7 years"),
    ('8', "8 years"),
)

JOB_TYPE = (
    ('FT', "Full time"),
    ('PT', "Part time"),
    ('IT', "Internship"),
)

class Country(models.Model):
    """Model representing countries."""
    name = models.CharField(max_length=200, help_text='Name of countries.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Education(models.Model):
    """Model representing education."""
    name = models.CharField(max_length=200, help_text='Level of Education e.g. Graduation.')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Skill(models.Model):
    """Model representing countries."""
    name = models.CharField(max_length=200, help_text='Select your Skills e.g. IT, Machine Learning')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class JobSeeker(models.Model):
    """Model representing a job seeker"""
    fname = models.CharField(max_length=30,help_text='Enter your First Name')     #First Name of the job seeker
    mname = models.CharField(max_length=30,help_text='Enter your Middle Name')     #Middle Name of the job seeker
    lname = models.CharField(max_length=30,help_text='Enter your Last Name')     #Last Name of the job seeker
    gender = models.CharField(choices=GENDER, max_length=1)
    address = models.TextField(max_length=1000, help_text='Enter your Street Address')
    country = models.ManyToManyField(Country, help_text='Select your Country')
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })
    mobile = models.CharField(max_length=10,help_text='Enter your Mobile Number')
    experience = models.CharField(choices=EXP_YEARS, max_length=1)
    education = models.ManyToManyField(Education, help_text='Select your education')
    skills = models.ManyToManyField(Skill, help_text='Select your skills')

    status = models.CharField(choices=STATUS,  max_length=1)
    date_registration = models.DateField(null=True, blank=True)
    
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')

    class Meta:
        ordering = ['fname','lname']
    
    def __str__(self):
        """String for representing the Model object."""
        return self.fname

    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('user-detail', args=[str(self.id)])

class Company(models.Model):
    """Model representing a companies offering jobs"""
    cname = models.CharField(max_length=30,help_text='Company name')     #Company Name 
    contact = models.CharField(max_length=200,help_text='Contact information')     #contact information
    
    cdescription = models.TextField(max_length=2000,help_text='Add Company Description',default="Description: " )
    caddress = models.TextField(max_length=1000, help_text='Company Address')
    country = models.ManyToManyField(Country, help_text='Select your Country')
    email = models.EmailField(unique=True, blank=False,
                              error_messages={
                                  'unique': "A user with that email already exists.",
                              })    
    
    
    #job = models.ForeignKey('Job',related_name='company_added',on_delete=models.SET_NULL,blank=True,null=True)
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    #upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    
    class Meta:
        ordering = ['cname']


    def __str__(self):
        """String for representing the Model object."""
        return self.cname

    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('profiles:company-detail', args=[str(self.id)])


import uuid # Required for unique job instances

class Job(models.Model):
    """Model representing a specific job."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    
    company = models.ForeignKey('Company', related_name='company_created',on_delete=models.SET_NULL,blank=True,null=True)
    #jobseeker = models.ForeignKey('JobSeeker',related_name='person_applied', on_delete=models.SET_NULL,blank=True,null=True)

    location = models.CharField(max_length=200,help_text='Country name') 
    designation = models.CharField(max_length=200,help_text='Designation eg Developer, Full Stack')
    #date_joining = models.DateField(null=True, blank=True)
    date_loggedin = models.DateField(null=True, blank=True)
    job_description = models.TextField(max_length=2000,help_text='Add Job Description' )
    job_type = models.CharField(choices=JOB_TYPE,default='FT',max_length=2,blank=True,help_text='Type of job - Full Time/Part Time/Internship')
    exp_required = models.CharField(choices=EXP_YEARS, max_length=1)
    salary = models.CharField(max_length=30, blank=True)
    
    
    url = models.URLField(max_length=200,null=True, blank=True)

    last_date = models.DateField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    JOB_STATUS = (
        ('a', 'Available'),
        ('c', 'Closed'),
    )

    status = models.CharField(
        max_length=1,
        choices=JOB_STATUS,
        blank=True,
        default='a',
        help_text='position availability',
    )

    class Meta:
        ordering = ['date_loggedin']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.designation})'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('profiles:single-job', args=[str(self.id)])
    


class JobApplicant(models.Model):

    jobSeeker = models.ForeignKey(JobSeeker,related_name='person_applied', on_delete=models.CASCADE,null=True,blank =True)
    job = models.ForeignKey(Job,related_name='job_applied' ,on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return self.job.designation


  

class BookmarkJob(models.Model):

    jobSeeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __str__(self):
        return f'{self.job.id} ({self.job.designation})'


class Category(models.Model):
    name = models.CharField(max_length=50,help_text='Job Category name')

    def __str__(self):
        return self.name