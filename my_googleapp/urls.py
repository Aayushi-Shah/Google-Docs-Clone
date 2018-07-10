
from django.contrib import admin
from django.urls import path,include
from googledocsclone import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('googledocsclone.urls'))
]
