from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),
    path('', lambda request: redirect('film_list', permanent=False)),
]