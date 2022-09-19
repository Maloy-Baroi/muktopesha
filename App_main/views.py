import json
from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from App_auth.views import *
from App_auth.forms import *
from App_main.forms import *
from App_main.models import *
from datetime import date


today = date.today()
today_month = today.month
today_year = today.year
today_day = today.day

# Create your views here.
@login_required
def freelancer_home_view(request):
    if is_freelancer(request.user):
        if is_profile_filled(request.user):
            skill_categories = SkillCategoryModel.objects.all()
            profile = FreelancerProfileModel.objects.get(user=request.user)
            best_freelancer = FreelancerProfileModel.objects.filter(stars=1)[:20]
            content = {
                'profile': profile,
                'skill_categories': skill_categories,
                'best_freelancer': best_freelancer,
            }
            return render(request, 'App_main/Freelancer/freelancer_home.html', context=content)
        else:
            return HttpResponseRedirect(reverse('App_auth:profile-setup-view'))
    else:
        return redirect('/buyer')


@login_required
@user_passes_test(is_freelancer)
def find_all_jobs(request):
    jobs = JobModel.objects.filter(status='Requested')
    jobList = []
    for job in jobs:
        if today_day >= job.validate_until.day and today_month >= job.validate_until.month and today_year >= job.validate_until.year:
            if OfferedToDoTheJobModel.objects.filter(user=request.user, job=job).exists():
                pass
            else:    
                jobList.append(job)
    mySkills = SkillListModel.objects.filter(user=request.user)
    mySkillsCategories = set([x.category.categoryName for x in mySkills])
    myJobs = []
    for job in jobs:
        if job.sub_category.category.name in mySkillsCategories:
            myJobs.append(job)
    
    content = {
        'jobList': jobList,
        'jobs': myJobs,
    }
    return render(request, 'App_main/freelancer/find_all_jobs.html', context=content)


@login_required
def apply_job(request, id):
    job = JobModel.objects.get(id=id)
    if request.method == 'POST':
        extra_text = request.POST.get('offer-text')
        offer = OfferedToDoTheJobModel(job=job, user=request.user, offer_text=extra_text)
        offer.save()
        return HttpResponseRedirect(reverse('App_main:find-all-jobs'))
    return render(request, "jobs/job_apply.html")


def all_freelancer_view(request):
    freelancers = FreelancerProfileModel.objects.all()
    content = {
        'freelancers': freelancers,
    }
    return render(request, 'App_main/Freelancer/all_freelancer.html', context=content)



@login_required
def buyer_home_view(request):
    if is_buyer(request.user):
        if is_profile_filled(request.user):
            skill_categories = SkillCategoryModel.objects.all()
            best_freelancer = FreelancerProfileModel.objects.filter(stars=1)[:20]
            content = {
                'skill_categories': skill_categories,
                'best_freelancer': best_freelancer,
            }
            return render(request, 'App_main/Buyer/buyer_home.html', context=content)
        else:
            return HttpResponseRedirect(reverse('App_auth:profile-setup-view'))
    else:
        return redirect('/')
        



def buyer_job_post(request):
    form = JobModelForm()
    newBudget = 0
    if request.method == 'POST':
        form = JobModelForm(request.POST, request.FILES)
        if form.is_valid():
            thisForm = form.save(commit=False)
            budget = form.cleaned_data.get('budget')
            if budget%5 <= 2:
                r = budget//5
                newBudget = r*5
            else:
                r= budget // 5
                newBudget = (r+1)*5
            thisForm.author = request.user
            thisForm.status = "Requested"
            thisForm.budget = newBudget
            thisForm.save()
            return HttpResponseRedirect(reverse('App_main:buyer-home'))
    
    content = {
        'form': form,
    }
    return render(request, 'App_main/Buyer/buyer_job_post_view.html', context=content)



def buyer_finds_freelancer(request):
    freelancers = FreelancerProfileModel.objects.all()
    content = {
        'freelancers': freelancers,
    }
    return render(request, 'App_main/Buyer/buyer_finds_freelancer.html', context=content)


