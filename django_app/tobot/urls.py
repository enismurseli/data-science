# tobot/urls.py
from django.urls import path
from .views import post_list, home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/', post_list, name='post_list'),
    path('home/', home, name='home'),
]


