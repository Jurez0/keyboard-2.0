from django.urls import path

from . import views

app_name = 'home_main'

urlpatterns = [
    path('', views.product_all, name='home_main')

]