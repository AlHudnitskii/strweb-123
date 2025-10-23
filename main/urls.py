from django.urls import re_path, path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('popular/', views.popular_list, name='popular_list'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
    re_path(r'^shop/$', views.product_list, name='product_list'),
    re_path(r'^shop/(?P<slug>[\w-]+)/$', views.product_detail, name='product_detail'),
    re_path(r'^shop/category/(?P<category_slug>[\w-]+)/$', views.product_list, name='product_list_by_category'),
    path('about/', views.about, name='about'),
    path('news/', views.news, name='news'),  
    path('terms/', views.terms, name='terms'),
    path('contacts/', views.contacts, name='contacts'),
    path('vacancies/', views.vacancies, name='vacancies'),
    path('promocodes/', views.promocodes, name='promocodes'),
    path('reviews/', views.reviews, name='reviews'),
    path('statistics/', views.statistics, name='statistics'),
    path('privacy/', views.privacy, name='privacy'),
    path('api/employee-data/', views.employee_data_json, name='employee_data_json'),    
]