from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(JobCategoriesModel)
admin.site.register(SubCategoriesModel)
admin.site.register(JobModel)
admin.site.register(OfferedToDoTheJobModel)
