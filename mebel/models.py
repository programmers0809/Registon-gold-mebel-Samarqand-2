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
    client_name = models.CharField(max_length=100, verbose_name='Mijoz ismi')
    profession = models.CharField(max_length=100, verbose_name='Kasbi')
    image = models.ImageField(upload_to='testimonials/', verbose_name='Rasmi')  # MEDIA settings kerak
    feedback = models.TextField(verbose_name='Fikr-mulohaza')

    def __str__(self):
        return self.client_name

    class Meta:
        db_table = 'izoxlar'
        managed = True
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'


class ContactModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ismingiz")
    email = models.EmailField(verbose_name="Email Manzilingiz")
    phone = models.CharField(max_length=15, verbose_name="Telefon Raqamingiz")
    furniture_type = models.CharField(
        max_length=50,
        choices=[
            ("1", "Yotoq Mebellari"),
            ("2", "Oshxona Mebellari"),
            ("3", "Ofis Mebellari"),
            ("4", "Shkaflar"),
            ("5", "Stullar va Jadvallar"),
        ],
        verbose_name="Mebel Turi",
    )
    message = models.TextField(blank=True, verbose_name="Maxsus Izohlaringiz")

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        db_table = 'aloqa'
        managed = True
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'
