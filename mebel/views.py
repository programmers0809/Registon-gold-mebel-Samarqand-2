from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import ServiceModel, CategoryModel, Testimonial, TeamMemberModel,Product
from .forms import ContactModelForm, TestimonialForm
class HomeView(View):
    def get(self, request):
        """ GET so‘rovi uchun sahifani ma'lumotlar bilan yuklash """
        context = {
            'services_page': ServiceModel.objects.all(),
            'category_page': CategoryModel.objects.all(),
            'testimonials': self.get_testimonials_with_stars(),
            'inquiry_form': ContactModelForm(),
            'team_page': TeamMemberModel.objects.all(),
            'products': Product.objects.all(),
        }
        return render(request, 'index.html', context)

    def post(self, request):
        """ POST so‘rovi orqali formani qayta ishlash """
        inquiry_form = ContactModelForm(request.POST)

        if inquiry_form.is_valid():
            inquiry_form.save()
            return redirect('home_page')  # Muvaffaqiyatli qo‘shilganidan keyin qayta yo‘naltirish
        
        # Form xatolar bilan qaytariladi
        context = {
            'services_page': ServiceModel.objects.all(),
            'category_page': CategoryModel.objects.all(),
            'testimonials': self.get_testimonials_with_stars(),
            'inquiry_form': inquiry_form,
            'team_page': TeamMemberModel.objects.all(),
            'products': Product.objects.all(),
        }
        return render(request, 'index.html', context)

    def get_testimonials_with_stars(self):
        """ Izohlarga yulduzcha reytingini qo‘shib beradi """
        testimonials = Testimonial.objects.all()
        for testimonial in testimonials:
            testimonial.full_stars = range(testimonial.rating // 20)  # To‘liq yulduzlar
            testimonial.empty_stars = range(5 - (testimonial.rating // 20))  # Bo‘sh yulduzlar
        return testimonials

class ContactView(View):
    def get(self, request):
        form = ContactModelForm()
        category_page = CategoryModel.objects.all()

        context = {
            'form': form,
            'category_page': category_page,
        }
        return render(request, 'contact.html', context)

    def post(self, request):
        form = ContactModelForm(request.POST)
        category_page = CategoryModel.objects.all()  # Kategoriya ma'lumotlarini qo'shish

        if form.is_valid():
            form.save()
            return redirect('home_page')

        return render(request, 'contact.html', {'form': form, 'category_page': category_page})



    
class AboutView(View):
    def get(self, request):
        # Retrieve data from the database
        category_page = CategoryModel.objects.all()
        team_page = TeamMemberModel.objects.all()
        testimonials = Testimonial.objects.all()

        # Modify testimonials for star ratings
        for testimonial in testimonials:
            testimonial.full_stars = range(testimonial.rating // 20)  # To'liq yulduzlar
            testimonial.empty_stars = range(5 - (testimonial.rating // 20))  # Bo'sh yulduzlar

        # Organize data into context
        context = {
            'category_page': category_page,
            'team_page': team_page,
            'testimonials': testimonials,  # Testimonialni qo'shish
        }

        # Render the template with the context
        return render(request, 'about.html', context)


    

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
    
    
    


