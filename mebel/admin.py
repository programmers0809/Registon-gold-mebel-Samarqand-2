from django.contrib import admin

from .models import ServiceModel, CategoryModel, Testimonial, ContactModel, TeamMemberModel
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




@admin.register(ContactModel)
class FurnitureInquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'furniture_type', 'message')
    list_filter = ('furniture_type',)  # Mebel turlariga ko‘ra filtr
    search_fields = ('name', 'email', 'phone', 'message')  # Qidiruv
    ordering = ('-id',)  # Yangi qo‘shilganlar yuqorida ko‘rinadi


@admin.register(TeamMemberModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')
