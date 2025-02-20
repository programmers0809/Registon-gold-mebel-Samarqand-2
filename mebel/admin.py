from django.contrib import admin
from .models import ServiceModel, CategoryModel, Testimonial, ContactModel, TeamMemberModel, Product

# ServiceModel uchun admin klass
@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category')
    search_fields = ('title',)
    list_filter = ('category',)
    ordering = ('title',)  # Alfavit bo‘yicha tartib

# CategoryModel uchun admin klass
@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Testimonial uchun admin klass
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'rating', 'image')
    search_fields = ('client_name', 'feedback')
    ordering = ('client_name',)
    fields = ('client_name', 'image', 'feedback', 'rating')

# ContactModel uchun admin klass
@admin.register(ContactModel)
class FurnitureInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'furniture_type', 'message')
    list_filter = ('furniture_type',)
    search_fields = ('name', 'email', 'phone', 'message')
    ordering = ('-id',)

# TeamMemberModel uchun admin klass
@admin.register(TeamMemberModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
    search_fields = ('name', 'designation')

# Mahsulotlar admin panelida qanday ko'rinishda bo'lishini belgilash
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'updated_at', 'video')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    list_per_page = 20  # Har bir sahifada 20 mahsulot
