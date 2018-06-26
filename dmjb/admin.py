from django.contrib import admin
from dmjb.models import Job

# Register your models here.


class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Job, JobAdmin)


