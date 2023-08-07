from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.product_all, name='products'),
    # path('filter/',views.product_filtered, name='filtered'),


]