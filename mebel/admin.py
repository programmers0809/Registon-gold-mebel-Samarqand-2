from django.contrib import admin
from .models import ServiceModel, CategoryModel, Testimonial, ContactModel, TeamMemberModel,Product

# ServiceModel uchun admin klass
@admin.register(ServiceModel)  # Dekorator yordamida registratsiya
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category')  # 'category' maydoni qo'shildi
    search_fields = ('title',)  
    list_filter = ('category',)  # Filtrlash uchun 'category' maydoni qo'shildi

# CategoryModel uchun admin klass
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Kategoriyaning nomini ko'rsatadi
    search_fields = ('name',)  # Kategoriyalarni qidirish uchun

# Testimonial uchun admin klass
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession')

# ContactModel uchun admin klass
@admin.register(ContactModel)
class FurnitureInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'furniture_type', 'message')
    list_filter = ('furniture_type',)  # Mebel turlariga ko‘ra filtr
    search_fields = ('name', 'email', 'phone', 'message')  # Qidiruv
    ordering = ('-id',)  # Yangi qo‘shilganlar yuqorida ko‘rinadi

# TeamMemberModel uchun admin klass
@admin.register(TeamMemberModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')

# Mahsulotlar admin panelida qanday ko'rinishda bo'lishini belgilash
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at', 'video')  # Ustunlar
    search_fields = ('name', 'description')  # Qidirish maydonlari
    list_filter = ('created_at', 'updated_at')  # Filtrlash
    ordering = ('-created_at',)  # Avtomatik ravishda yaratish sanasi bo'yicha tartiblash

# Modelni admin paneliga qo'shish
admin.site.register(Product, ProductAdmin)