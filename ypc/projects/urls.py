"""ypc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
	path('<int:pk>/', views.project_detail, name='project_detail'),
	path('new/', views.project_new, name='project_new'),
	path('<int:pk>/edit/', views.project_edit, name='project_edit'),
	path('<int:pk>/remove/', views.project_remove, name='project_remove'),
]
