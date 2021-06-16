from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path('', views.index, name='index' ),
    path('jobs/', views.JobListView.as_view(), name='jobs'),
    path('job/<uuid:pk>', views.JobDetailView.as_view(), name='single-job'),
    path('companys/', views.CompanyListView.as_view(), name='companys'),
    path('company/<int:pk>', views.CompanyDetailView.as_view(), name='company-detail'),
    path('jobseeker/<int:pk>/create/', views.create_profile_View, name='user-detail'),
    path('company/<int:pk>/create/', views.create_company_View, name='company-register'),

]

urlpatterns += [
    #path('job/create/', views.create_job_View, name='create-job'),
    path('job/<int:pk>/create/', views.create_job_View, name='create-job'),
    path('jobapplicant/<uuid:id>/apply/', views.apply_job_View, name='apply-job'),
]

urlpatterns += [
   # path('jobseeker/create/', views.JobSeekerCreate.as_view(), name='jobseeker-create'),
    path('jobseeker/<int:pk>/update/', views.JobSeekerUpdate.as_view(), name='jobseeker-update'),
    path('jobseeker/<int:pk>/delete/', views.JobSeekerDelete.as_view(), name='jobseeker-delete'),
]




urlpatterns += [

   path('result/', views.search_result_view, name='search_result'),
   path('find_job/', views.find_job_view, name='find_job'),
    
]