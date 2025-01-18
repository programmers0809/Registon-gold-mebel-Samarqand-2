from django.contrib import admin

from .models import ServiceModel, CategoryModel,Testimonial


@admin.register(ServiceModel)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'category')  # 'category' maydoni qo'shildi
    search_fields = ('title',)  
    list_filter = ('category',)  # Filtrlash uchun 'category' maydoni qo'shildi


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Kategoriyaning nomini ko'rsatadi
    search_fields = ('name',)  # Kategoriyalarni qidirish uchun



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'profession')