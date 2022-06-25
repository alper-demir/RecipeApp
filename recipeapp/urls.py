from django.urls import path
from .import views

urlpatterns = [

    path('', views.index, name ='index'),
    path('home', views.index, name ='index'),
    path('sweet', views.sweet, name='sweet'),
    path('maincourse', views.maincourse, name='maincourse'),
    path('vegetable', views.vegetable, name='vegetable'),
    path('maincourse/<int:id>', views.maincourse_detail, name="maincourse_detail"),
    path('sweet/<int:id>', views.sweet_detail, name="sweet_detail"),
    path('vegetable/<int:id>', views.vegetable_detail, name="vegetable_detail"),
]