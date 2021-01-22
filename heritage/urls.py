from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('news/', views.news, name='news'),
    path('awwards/', views.awwards, name='awwards'),
    path('give/', views.give, name='give'),
    path('contact/', views.contact, name='contact'),
]