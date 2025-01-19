from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import ServiceModel, CategoryModel, Testimonial, ContactModel

from .forms import ContactModelForm

class HomeView(View):
    def get(self, request):
        # Model ma’lumotlarini olish
        services_page = ServiceModel.objects.all()
        category_page = CategoryModel.objects.all()
        testimonials = Testimonial.objects.all()

        # FurnitureInquiryForm uchun bo‘sh forma
        inquiry_form = ContactModelForm()

        context = {
            'services_page': services_page,
            'category_page': category_page,
            'testimonials': testimonials,
            'inquiry_form': inquiry_form,
        }
        return render(request, 'index.html', context=context)

    def post(self, request):
        # FurnitureInquiryForm ni to‘ldirish va saqlash
        inquiry_form = ContactModelForm(request.POST)
        if inquiry_form.is_valid():
            inquiry_form.save()
            return redirect('home_page')  # Saqlangandan keyin bosh sahifaga qaytish

        # Agar forma xato bo‘lsa, avvalgi ma’lumotlarni yuklash
        services_page = ServiceModel.objects.all()
        category_page = CategoryModel.objects.all()
        testimonials = Testimonial.objects.all()

        context = {
            'services_page': services_page,
            'category_page': category_page,
            'testimonials': testimonials,
            'inquiry_form': inquiry_form,
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
