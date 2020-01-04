from django.contrib import admin
from django.urls import path
from display_droplets.views import GetDroplets

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', GetDroplets.as_view(template_name='droplets.html'), name='Droplet View'),
]