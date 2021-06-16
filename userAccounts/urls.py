from django.urls import path
from userAccounts import views

app_name = "userAccounts"

urlpatterns = [

    path('user/register/', views.user_registration, name='user-registration'),
    path('employer/register/', views.employer_registration, name='company-registration'),
    #path('profile/edit/<int:id>/', views.employee_edit_profile, name='edit-profile'),
    path('login/', views.user_logIn, name='login'),
    path('logout/', views.user_logOut, name='logout'),
]
