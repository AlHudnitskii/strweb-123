from django.contrib import admin

from .models import (
   Product, Category, Article, Employee,
   Vacancy, PromoCode, Term, Review,
   CompanyHistory, CompanyInfo, Partner, Banner,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
<<<<<<< HEAD
   list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'discount']
   list_filter = ['available', 'created', 'updated']
   list_editable = ['price', 'available', 'discount']   
   prepopulated_fields = {'slug' : ("name",)}
   
admin.site.register(Article)   
admin.site.register(Employee)
admin.site.register(Vacancy)
admin.site.register(PromoCode)
admin.site.register(Term)
admin.site.register(Review)
admin.site.register(CompanyHistory)
admin.site.register(CompanyInfo)
admin.site.register(Partner)
admin.site.register(Banner)
=======
    list_display = [
        "name",
        "slug",
        "price",
        "available",
        "created",
        "updated",
        "discount",
    ]
    list_filter = ["available", "created", "updated"]
    list_editable = ["price", "available", "discount"]
    prepopulated_fields = {"slug": ("name",)}
>>>>>>> 253d1c02d106f490a99efe7e4293e81c275e3c5c
