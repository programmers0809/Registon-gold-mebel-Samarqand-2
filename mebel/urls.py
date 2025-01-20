from django.urls import path

from .views import HomeView, CategoryDetailView, AboutView, ContactView, ServiceView

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('service/', ServiceView.as_view(), name='service_page'),
    path('category/', CategoryDetailView.as_view(), name='category_detail'),
]
