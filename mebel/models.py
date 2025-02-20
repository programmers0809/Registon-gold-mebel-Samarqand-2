from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


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
    image = models.ImageField(
        upload_to='testimonials/', 
        verbose_name='Rasmi', 
        default='testimonials/default.jpg'
    )
    feedback = models.TextField(verbose_name='Fikr-mulohaza')
    rating = models.PositiveIntegerField(
        verbose_name='Reyting (%)', 
        default=0,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.client_name

    class Meta:
        db_table = 'izoxlar'
        managed = True
        verbose_name = 'Izoh'
        verbose_name_plural = 'Izohlar'
        ordering = ['-rating']  # Eng yuqori reytingga ega sharhlar birinchi chiqadi


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


class TeamMemberModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ism")
    designation = models.CharField(max_length=100, verbose_name="Lavozim")
    image = models.ImageField(upload_to='team/', verbose_name="Rasm")
    facebook_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Facebook havola")
    twitter_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Twitter havola")
    instagram_url = models.URLField(max_length=200, blank=True, null=True, verbose_name="Instagram havola")

    def __str__(self):
        return self.name
      
    class Meta:
        db_table = 'Jamolar'  # Table name in the database
        managed = True  # Allows Django to manage the table (migrations)
        verbose_name = 'Team Member'  # Singular form for one member
        verbose_name_plural = 'Bizning Jamolar'  # Plural form for all team members



class Product(models.Model):
    name = models.CharField(max_length=100)  # Mahsulot nomi
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Narxi
    description = models.TextField(blank=True, null=True)  # Tavsifi
    created_at = models.DateTimeField(auto_now_add=True)  # Yaratilgan vaqt
    updated_at = models.DateTimeField(auto_now=True)  # Yangilangan vaqt
    video = models.FileField(upload_to='videos/', blank=True, null=True)  # Video fayli

    def __str__(self):
        return self.name  # Model obyekti uchun nom qaytaradi
    


    class Meta:
        db_table = 'Maxsulot'  # Table name in the database
        managed = True  # Allows Django to manage the table (migrations)
        verbose_name = 'Team Member'  # Singular form for one member
        verbose_name_plural = 'Bizning Maxsulaotlar'  # Plural form for all team members