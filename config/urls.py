"""
config URL Configuration
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from users import views as user_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('lessons.urls')),
    path('register/', user_view.register, name="users-register"),
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'),
         name="users-login"),
    path('logout/',
         auth_views.LogoutView.as_view(template_name='users/logout.html'),
         name="users-logout"),
    path('profile/', user_view.profile, name="users-profile")
]
