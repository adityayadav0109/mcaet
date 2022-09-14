from django.urls import path
from main import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ug/',views.ug_course, name='ug'),
    path('pg/',views.pg_course, name="pg"),
    path('gallery/',views.gallery, name="gallery"),
    path('faculty/',views.faculty, name="faculty"),
    path('contact/',views.contact, name="contact"),
    path('about-university/',views.about_uni, name="about_uni"),
    path('about-college/',views.about_clg, name="about_clg"),
    path('about-developer/',views.about_dev, name="about_dev"),
]