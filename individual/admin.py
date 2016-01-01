from django.contrib import admin

from individual.models import Individual

class IndividualAdmin(admin.ModelAdmin):
    pass
admin.site.register(Individual, IndividualAdmin)
