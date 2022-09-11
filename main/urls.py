from django.urls import path
from main import views

urlpatterns = [
    path('',views.home, name="home"),
    path('ug/',views.ug_course, name='ug'),
    path('pg/',views.pg_course, name="pg"),
]