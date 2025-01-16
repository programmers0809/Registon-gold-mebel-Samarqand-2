from django.shortcuts import render
from django.views import View

from .models import ServiceModel

class HomeView(View):
    def get(self, request):
        
        services_page = ServiceModel.objects.all() 
        
        context = {
            'services_page': services_page,
        }
        
        return render(request, 'index.html', context=context)
    
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    
class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
    
class ServiceView(View):
    def get(self, request):
        
        services_page = ServiceModel.objects.all() 
        
        context = {
            'services_page': services_page,
        }
        return render(request, 'service.html', context=context)
    
class CategoryDetailView(View):
    def get(self, request):
        return render(request, 'category_detail.html')
