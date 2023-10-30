from django.contrib import admin
from django.urls import path, include
from . import code_views

urlpatterns = [
    path('<int:key>/', code_views.source, name = 'repo_code_view'),
    path('search/', code_views.search_by_keywords, name = 'repo_search_by_keys'),
    path('<int:key>/update/', code_views.update_source, name = 'repo_code_update_source'),
    path('add/', code_views.add, name = 'repo_code_add'),
    path('update/<int:key>/', code_views.update, name = 'repo_code_update'),
    path('delete/<int:key>/', code_views.delete, name = 'repo_code_delete')
]
