from django.contrib import admin

from .models import ServiceModel

@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image') 
    search_fields = ('title',)  
    list_filter = ('title',)  
