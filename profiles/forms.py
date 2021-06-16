from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from profiles.models import *

import datetime

from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class JobForm(forms.Form):
    JOB_TYPE = (
    ('FT', "Full time"),
    ('PT', "Part time"),
    ('IT', "Internship"),
    )
    #id = forms.UUIDField()
    designation=forms.CharField(label='Designation', max_length=100)
    location=forms.CharField(label='Location', max_length=100)
    job_description=forms.CharField(widget=forms.Textarea)
    last_date = forms.DateField(label='Submission Date')
    exp_required=forms.CharField(label='Experience Required', max_length=1)
    salary=forms.CharField(label='Salary', max_length=30)
    job_type=forms.ChoiceField(label='JobType',choices=JOB_TYPE)
    
    
     
class JobSeekerForm(forms.Form):
    
    GENDER = (
    ('M', "Male"),
    ('F', "Female"),
    )
    INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
    fname = forms.CharField(label='First Name')     #First Name of the job seeker
    mname = forms.CharField(label='Middle Name')     #Middle Name of the job seeker
    lname = forms.CharField(label='Last Name')     #Last Name of the job seeker
    gender = forms.ChoiceField(label='Gender',choices=GENDER)
    address = forms.CharField(label='Address')
    country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('name'))
    #country = forms.CharField(label='Country', help_text='Select your Country')
    email=forms.EmailField(label='Email :', max_length=30)
    mobile = forms.CharField(label='Phone')
    #experience = forms.CharField(label='Experience')
    experience=forms.IntegerField(label="Experience", widget=forms.Select(choices=INTEGER_CHOICES))
    education = forms.ModelChoiceField(queryset=Education.objects.all().order_by('name'))
    #education = forms.CharField(label='Qualification', help_text='Select your education')
    #skills = forms.CharField(label='Skills', help_text='Select your skills')
    skills = forms.ModelChoiceField(queryset=Skill.objects.all().order_by('name'))
    #add resume and photo



class CompanyForm(forms.Form):
    
    cname = forms.CharField(label='Company Name :')     
    contact = forms.CharField(label='Contact Info :')     
    cdescription = forms.CharField(label='Description :',widget=forms.Textarea)     
    caddress = forms.CharField(label='Address :')
    country = forms.ModelChoiceField(queryset=Country.objects.all().order_by('name'))
    email=forms.EmailField(label='Email :', max_length=30)
    mobile = forms.CharField(label='Phone :')
    
  
        
class JobApplicantForm(forms.ModelForm):
    
    class Meta:
        model = JobApplicant
        fields = ['job']
    





