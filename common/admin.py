from django.contrib import admin

from common.models import Country, Type

class CountryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Country, CountryAdmin)

class TypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(Type, TypeAdmin)
