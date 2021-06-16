from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from userAccounts.models import User
from django.contrib.auth import get_user_model



class UserLoginForm(forms.Form):
    email =  forms.EmailField(widget=forms.EmailInput(attrs={ 'placeholder':'Email',}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder':'Password',}))

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("User Does Not Exist.")

            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")

            if not user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user

class UserRegistrationForm(UserCreationForm):
    GENDER = (
    ('M', "Male"),
    ('F', "Female"),

    )
    

    first_name=forms.CharField(label='First Name', max_length=100)
    last_name=forms.CharField(label='Last Name', max_length=100)
    
    email=forms.EmailField(label='Email :', max_length=30)
    gender=forms.ChoiceField(label='Gender :',choices=GENDER)
    role='RegisteredUser'
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))
    
    class Meta(UserCreationForm.Meta):
            model = User
            fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender']

    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        if commit:
            user.save()
        return user


class CompanyRegistrationForm(UserCreationForm):
    
    first_name=forms.CharField(label='Company Name :', max_length=100)
    #last_name=forms.CharField(label='Address :', max_length=100)
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input-text with-border', 'placeholder': 'Repeat Password'}))
    
    email=forms.EmailField(label='Email :', max_length=30)
    
    role='Employer'

    class Meta(UserCreationForm.Meta):
            model = User
            fields = ['first_name', 'email', 'password1', 'password2']

    
    def save(self, commit=True):
        user = UserCreationForm.save(self,commit=False)
        if commit:
            user.save()
        return user
