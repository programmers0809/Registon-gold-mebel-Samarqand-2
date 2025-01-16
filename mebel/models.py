from django.db import models


class ServiceModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Nomi')
    description = models.TextField(verbose_name='Ma\'lumot')  
    image = models.ImageField(upload_to='services/', verbose_name='Rasmi') 

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Service'
        managed = True
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislar'
