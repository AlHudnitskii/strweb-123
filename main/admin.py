from django.contrib import admin
from .models import (
    Category, Product, Article, Employee, Vacancy,
    PromoCode, Term, Review, CompanyInfo, CompanyHistory,
    Partner, Banner
)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available', 'created', 'updated', 'discount')
    list_filter = ('available', 'created', 'updated', 'category')
    search_fields = ('name', 'description')
    list_editable = ('price', 'available', 'discount')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    search_fields = ('title', 'short_info')
    list_filter = ('created_at', 'updated_at')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email')
    search_fields = ('name', 'position')


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title',)


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'is_active', 'valid_until')
    list_filter = ('is_active', 'valid_until')
    search_fields = ('code', 'description')


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('question', 'added_at')
    search_fields = ('question', 'answer')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('user__username', 'text')


class CompanyHistoryInline(admin.TabularInline):
    model = CompanyHistory
    extra = 1


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [CompanyHistoryInline]


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')
    search_fields = ('name',)


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('title',)
