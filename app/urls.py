from django.urls import  path
from app import views


urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('contact', views.contact),
    path('jobs',views.jobs),
    path('read',views.read)
]