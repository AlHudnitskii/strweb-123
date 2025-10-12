from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ["name"]
        indexes = [models.Index(fields=["name"])]
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        return reverse("main:product_list_by_category", args=[self.slug])

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products/%Y/%m/%d", blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["id", "slug"]),
            models.Index(fields=["name"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return f'{self.name}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    short_info = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
      name = models.CharField(max_length=100)
      position = models.CharField(max_length=100)
      photo = models.ImageField(upload_to='employees/', blank=True, null=True)
      phone = models.CharField(max_length=30)
      email = models.EmailField()
      description = models.TextField(blank=True)
   
      def __str__(self):
         return self.name    
      
class Vacancy(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   published_at = models.DateTimeField(auto_now_add=True)

   class Meta:
      ordering = ['-published_at']
      verbose_name = 'vacancy'
      verbose_name_plural = 'vacancies'
   
   def __str__(self):
      return self.title
   
   
class PromoCode(models.Model):
   code = models.CharField(max_length=50, unique=True)
   description = models.CharField(max_length=255)
   is_active = models.BooleanField(default=True)
   valid_until = models.DateField(null=True, blank=True)
   
   class Meta:
      ordering = ['-valid_until']
      verbose_name = 'promocode'
      verbose_name_plural = 'promocodes'
   
   def __str__(self):
      return self.code
   
class Term(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
      
class Review(models.Model):
      user = models.ForeignKey('users.User', on_delete=models.CASCADE)
      rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
      text = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)

      class Meta:
         ordering = ['-created_at']
         verbose_name = 'review'
         verbose_name_plural = 'reviews'
      
      def __str__(self):
         return f"{self.user.username} ({self.rating})"      
      
class CompanyInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.ImageField(upload_to='company/', blank=True, null=True)
    video = models.FileField(upload_to='company/', blank=True, null=True)
    details = models.TextField(help_text="Detailed information about the company")
    certificate = models.ImageField(upload_to='company/', blank=True, null=True)

    def __str__(self):
        return self.name

class CompanyHistory(models.Model):
    company = models.ForeignKey(CompanyInfo, on_delete=models.CASCADE, related_name='history')
    year = models.PositiveIntegerField()
    event = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.year}: {self.event}"
     
     
class Partner(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField()
    logo = models.ImageField(upload_to='partners/')
    
    def __str__(self):
        return self.name

class Banner(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='banners/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
