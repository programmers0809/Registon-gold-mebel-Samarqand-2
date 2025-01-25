from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import ServiceModel, CategoryModel, Testimonial, TeamMemberModel,Product
from .forms import ContactModelForm, TestimonialForm
class HomeView(View):
    def get(self, request):
        # Retrieve data from the database
        services_page = ServiceModel.objects.all()
        category_page = CategoryModel.objects.all()
        testimonials = Testimonial.objects.all()
        inquiry_form = ContactModelForm()  # Blank form for GET request
        team_page = TeamMemberModel.objects.all()
        products = Product.objects.all()  # Mahsulotlar

        # Organize data into context
        context = {
            'services_page': services_page,
            'category_page': category_page,
            'testimonials': testimonials,
            'inquiry_form': inquiry_form,
            'team_page': team_page,
            'products': products,  # Mahsulotlarni contextga qo'shish
        }

        # Render the template with the context
        return render(request, 'index.html', context)

    def post(self, request):
        # Handle form submission
        inquiry_form = ContactModelForm(request.POST)
        
        if inquiry_form.is_valid():
            # Process the data, e.g., save it to the database, send an email, etc.
            inquiry_form.save()  # Assuming the form saves the data to the database
            
            # Redirect or render a success page after processing the form
            return redirect('home_page')  # You can replace 'success_url' with your desired redirect URL
        else:
            # If the form is invalid, re-render the page with error messages
            services_page = ServiceModel.objects.all()
            category_page = CategoryModel.objects.all()
            testimonials = Testimonial.objects.all()
            team_page = TeamMemberModel.objects.all()

            # Pass the form with errors in the context
            context = {
                'services_page': services_page,
                'category_page': category_page,
                'testimonials': testimonials,
                'inquiry_form': inquiry_form,
                'team_page': team_page,
            }

            return render(request, 'index.html', context)


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
        team_page = TeamMemberModel.objects.all()
        
        
        context = {
            'category_page': category_page, 
            'team_page': team_page,
        }
        
        return render(request, 'about.html', context=context)
    

class ServiceView(View):
    def get(self, request):
        
        services_page = ServiceModel.objects.all()  # Xizmatlar
        testimonials = Testimonial.objects.all()  # Fikrlar
        category_page = CategoryModel.objects.all()  # Kategoriyalar
        products = Product.objects.all()  # Mahsulotlar

        context = {
            'services_page': services_page,
            'testimonials': testimonials,
            'category_page': category_page,
            'products': products,  # Mahsulotlarni contextga qo'shish
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
    
    
    
    