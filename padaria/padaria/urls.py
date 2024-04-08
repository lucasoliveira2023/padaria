from django.contrib import admin
from django.urls import path
from appinicial.views import inicio, Contato

urlpatterns = [

    path('', inicio, name='inicio'),
    path('pgcontato/', Contato, name='contato'),
    path('admin/', admin.site.urls),
]