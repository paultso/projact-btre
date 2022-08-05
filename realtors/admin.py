from django.contrib import admin

# Register your models here.
from .models import Realtor

# set the / api, as variable= index to callback function


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25


admin.site.register(Realtor, RealtorAdmin)
