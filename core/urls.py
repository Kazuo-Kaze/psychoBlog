from django.urls import path

from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('search/', views.search, name='search'),
    path('bio/', views.bio, name='bio'),
    path('contact/', views.contact, name='contact'),
    # path('collections/', views.collections, name='collections'),
    path('<slug:slug>/', views.categorydetails, name='details'),
    path('<slug:category_slug>/<slug:slug>/', views.details, name='details'),
]