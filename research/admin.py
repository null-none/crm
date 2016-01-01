from django.contrib import admin

from research.models import Research

class ResearchAdmin(admin.ModelAdmin):
    pass
admin.site.register(Research, ResearchAdmin)
