from django import forms
from .models import ContactModel,Testimonial

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'phone', 'furniture_type', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Ismingiz',
                'style': 'height: 55px;',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Email Manzilingiz',
                'style': 'height: 55px;',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Telefon Raqamingiz',
                'style': 'height: 55px;',
            }),
            'furniture_type': forms.Select(attrs={
                'class': 'form-select border-0',
                'style': 'height: 55px;',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control border-0',
                'placeholder': 'Maxsus Izohlaringiz',
                'rows': 4,
            }),
        }


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['client_name', 'profession', 'image', 'feedback', 'rating']
        widgets = {
            'client_name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Mijoz ismini kiriting'
            }),
            'profession': forms.Select(attrs={
                'class': 'form-control', 
                'placeholder': 'Kasbni tanlang'
            }),
            'feedback': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Fikr-mulohaza yozing', 
                'rows': 4
            }),
            'rating': forms.NumberInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Reyting (%) kiriting', 
                'min': 0, 
                'max': 100
            }),
        }




