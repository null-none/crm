from django.contrib import admin

from hr.models import Hr

class HrAdmin(admin.ModelAdmin):
    pass
admin.site.register(Hr, HrAdmin)
