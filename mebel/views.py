from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import ServiceModel, CategoryModel, Testimonial, TeamMemberModel
from .forms import ContactModelForm, TestimonialForm

class HomeView(View):
    def get(self, request):
        # Model ma’lumotlarini olish
        services_page = ServiceModel.objects.all()
        category_page = CategoryModel.objects.all()
        testimonials = Testimonial.objects.all()
        inquiry_form = ContactModelForm()
        team_page = TeamMemberModel.objects.all()

        context = {
            'services_page': services_page,
            'category_page': category_page,
            'testimonials': testimonials,
            'inquiry_form': inquiry_form,
            'team_page': team_page,
        }
        return render(request, 'index.html', context=context)



class ContactView(View):
    def get(self, request):
      
        form = ContactModelForm() 
        category_page = CategoryModel.objects.all()
        
        
        context = {
            'form': form,
            'category_page': category_page, 
        }
        return render(request, 'contact.html', context=context)

    def post(self, request):
    
        inquiry_form = ContactModelForm(request.POST) 
        if inquiry_form.is_valid(): 
            inquiry_form.save()  #
            return redirect('home_page')  
     
        return render(request, 'contact.html', {'form': inquiry_form})



    
    
    
class AboutView(View):
    def get(self, request):
        
        category_page = CategoryModel.objects.all()
        
        context = {
            'category_page': category_page, 
        }
        
        return render(request, 'about.html', context=context)
    

    
class ServiceView(View):
    def get(self, request):
        
        services_page = ServiceModel.objects.all() 
        testimonials = Testimonial.objects.all()
        category_page = CategoryModel.objects.all()

      
        context = {
            'services_page': services_page,
            'testimonials': testimonials,
            'category_page': category_page, 
            
        }
        return render(request, 'service.html', context=context)
    
class CategoryDetailView(View):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        form = TestimonialForm()
        category_page = CategoryModel.objects.all()
        
        context = {
            'category_page': category_page, 
            'form': form,
            'testimonials': testimonials
        }
        return render(request, 'category_detail.html', context=context)

    def post(self, request):
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_detail')  
        testimonials = Testimonial.objects.all()
        return render(request, 'category_detail.html', {'testimonials': testimonials, 'form': form})
    
    
    
    