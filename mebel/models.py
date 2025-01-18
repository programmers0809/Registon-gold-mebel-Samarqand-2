from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Kategoriya nomi')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        managed = True
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'


class ServiceModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nomi')
    description = models.TextField(verbose_name='Ma\'lumot')  
    image = models.ImageField(upload_to='services/', verbose_name='Rasmi')
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='services', verbose_name='Kategoriya')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Service'
        managed = True
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislar'

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')  # Ensure MEDIA settings are configured
    feedback = models.TextField()

    def __str__(self):
        return self.client_name