from django.contrib import admin
from django.urls import path, include
from . import tag_views

urlpatterns = [
    path('<int:key>/', tag_views.tag_results, name = 'repo_tag_view'),
    path('all/', tag_views.all_tags, name = 'repo_tag_all'),
    path('add/', tag_views.add, name = 'repo_tag_add'),
    path('update/<int:pk>', tag_views.upd, name = 'repo_tag_upd'),
    path('delete/<int:pk>', tag_views.delete, name = 'repo_tag_delete')
]
