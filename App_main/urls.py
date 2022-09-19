from django.urls import path
from App_main.views import *

app_name = 'App_main'

urlpatterns = [
    # Freelancer App_main
    path('', freelancer_home_view, name='freelancer-home'),
    path('find-all-jobs/', find_all_jobs, name='find-all-jobs'),
    path('apply-job/<int:id>/', apply_job, name='apply-job'),
    path('all-freelancer-view/', all_freelancer_view, name='all-freelancer-view'),



    # Buyer App_main
    path('buyer/', buyer_home_view, name='buyer-home'),
    path('buyer-job-post/', buyer_job_post, name='buyer-job-post'),
    path('buyer-finds-freelancer/', buyer_finds_freelancer, name='buyer-finds-freelancer'),
]

