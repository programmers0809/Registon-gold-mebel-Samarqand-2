from django.shortcuts import render
from django.views import View
from django.shortcuts import render, redirect
from .models import ServiceModel, CategoryModel, Testimonial, ContactModel

from .forms import ContactModelForm, TestimonialForm

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



class ContactView(View):
    def get(self, request):
        """
        GET so'rov: Foydalanuvchiga bo'sh formani ko'rsatish uchun ishlatiladi.
        """
        form = ContactModelForm()  # Bo'sh forma yaratish
        return render(request, 'contact.html', {'form': form})

    def post(self, request):
        """
        POST so'rov: Foydalanuvchi tomonidan yuborilgan ma'lumotlarni qabul qilish va saqlash uchun ishlatiladi.
        """
        inquiry_form = ContactModelForm(request.POST)  # Foydalanuvchi ma'lumotlarini qabul qilish
        if inquiry_form.is_valid():  # Forma validligini tekshirish
            inquiry_form.save()  # Ma'lumotlarni bazaga saqlash
            return redirect('home_page')  # Saqlangandan keyin bosh sahifaga qaytarish
        # Agar forma xato bo'lsa, xatolar bilan birga sahifani qayta ko'rsatish
        return render(request, 'contact.html', {'form': inquiry_form})



    
    
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
    

    
class ServiceView(View):
    def get(self, request):
        
        services_page = ServiceModel.objects.all() 
        testimonials = Testimonial.objects.all()
        
        context = {
            'services_page': services_page,
              'testimonials': testimonials,
        }
        return render(request, 'service.html', context=context)
    
class CategoryDetailView(View):
    def get(self, request):
        testimonials = Testimonial.objects.all()
        form = TestimonialForm()
        return render(request, 'category_detail.html', {'testimonials': testimonials, 'form': form})

    def post(self, request):
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category_detail')  
        testimonials = Testimonial.objects.all()
        return render(request, 'category_detail.html', {'testimonials': testimonials, 'form': form})