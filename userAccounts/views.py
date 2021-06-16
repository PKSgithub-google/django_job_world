
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect , get_object_or_404
from django.urls import reverse, reverse_lazy
from django.conf import settings

from userAccounts.forms import *
from profiles.permission import user_is_registered 
User = get_user_model()

#Handle Success Url After Sign In
def get_success_url(request):

    if 'next' in request.GET and request.GET['next'] != '':
        return request.GET['next']
    else:
        return reverse('profiles:index')



#Provides users to logIn
def user_logIn(request):

    form = UserLoginForm(request.POST or None)
    
    #print("-------1.......")
    if request.user.is_authenticated:
        #return redirect('/profiles')
        #print("-------2.......")
        return HttpResponseRedirect(reverse("profiles:index"))
    else:
        if request.method == 'POST':
            if form.is_valid():
                #print("-------3.......")
                auth.login(request, form.get_user())
                return HttpResponseRedirect(get_success_url(request))
    context = {
        'form': form,
    }

    return render(request,'registration/login.html',context)


def user_logOut(request):
    """
    Provide the ability to logout
    """
    auth.logout(request)
    messages.success(request, 'You are Successfully logged out')
    #return redirect('userAccounts:logout')
    #return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    #return render(request,'registration/logout.html',context)
    return(HttpResponseRedirect(reverse('userAccounts:logout')))



# Handle User Registration
def user_registration(request):

    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        
        return redirect(reverse('profiles:user-detail',kwargs={'pk': form.id}))
    context={
        
            'form':form,
            
        }

    return render(request,'registration/user-registration.html',context)

#Handle Employee Registration 
def employer_registration(request):

    form = CompanyRegistrationForm(request.POST or None)
    if form.is_valid():
        form = form.save()
        return redirect(reverse('profiles:company-register',kwargs={'pk': form.id}))
    context={
        
            'form':form
        }

    return render(request,'registration/company-registration.html',context)

