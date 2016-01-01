from django.contrib import admin

from designer.models import Designer

class DesignerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Designer, DesignerAdmin)
