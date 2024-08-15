from django.urls import  path
from app import views


urlpatterns = [
    path('',views.home),
    path('about',views.about),
    path('contact', views.contact),
    path('jobs',views.jobs),
    path('read',views.read),
    path('delete/<int:id>',views.remove),
    path('create',views.create, name="create"),
    path('update/<int:id>',views.update)
]