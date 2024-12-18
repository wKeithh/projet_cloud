"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views import login_view, logout_view
from .views import check_username
from .views import register_view
from documents.views import DocumentListCreateView, DocumentDetailView, DocumentUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', login_view, name='login'),  # Ajoute /api/ dans l'URL
    path('api/logout/', logout_view, name='logout'),  # URL de déconnexion
    path('api/register/', register_view, name='register'),  # Route d'inscription
    path('api/check-username/<str:username>/', check_username, name='check-username'),
    path('api/documents/', DocumentListCreateView.as_view(), name='document-list-create'),
    path('api/documents/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('api/documents/<int:pk>/', DocumentUpdateView.as_view(), name='document-update'),
]

