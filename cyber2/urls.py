"""cyber2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/home/slider/', views.dashboard_home_slider, name='dashboard/home/slider'),
    path('dashboard/home/slider/add/', views.dashboard_home_slider_add, name='dashboard/home/slider/add'),
    path('login/dashboard/', views.login_dashboard, name='login/dashboard'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/contact/', views.dashboard_contact, name = 'dashboard/cpntact' ),
    path('dashboard/contact/info/', views.dash_contact_info, name='dashboard/contact/info')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


