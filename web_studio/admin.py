from django.contrib import admin

from web_studio.models import WebStudio

class WebStudioAdmin(admin.ModelAdmin):
    pass
admin.site.register(WebStudio, WebStudioAdmin)
