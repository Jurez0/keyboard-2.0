from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('about/', include('about_us.urls')), 
    path('auth/', include('auth_sys.urls')), 
    path('cart/', include('cart.urls')),
    path('configurator/', include('configurator.urls')),
    path('', include('home_main.urls')),  

]
