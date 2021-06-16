from django.contrib import admin

from .models import JobSeeker, Company, Country, Education, Skill, Job, JobApplicant, Category, BookmarkJob

admin.site.register(Country)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(JobSeeker)
admin.site.register(Company)
admin.site.register(Job)
admin.site.register(JobApplicant)
admin.site.register(Category)
admin.site.register(BookmarkJob)
