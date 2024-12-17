from django.contrib import admin
from django.urls import path
from home import views as h_views
from course import views as c_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', h_views.index),
    path('', h_views.index),
    path('course/', c_views.index),
]