from django.contrib import admin
from django.urls import path, include
from . import views

handler404 = views.page_not_found

urlpatterns = [
    path('', views.inicio, name = 'repo_inicio'),
    path('code/', include('repo.code_urls')),
    path('tag/', include('repo.tag_urls')),
    path('preferences/', views.preferences, name = 'repo_preferences')
]
