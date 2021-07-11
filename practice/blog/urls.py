from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.main, name = 'main'),
    path('create/', views.create, name = 'create'),
    path('read/<int:blog_pk>/', views.read, name = 'read'),
    path('update/<int:blog_pk>/', views.update, name = 'update'),
    path('delete/<int:blog_pk>/', views.delete, name = 'delete'),
    path('comment_update/<int:comment_id>/', views.comment_update, name = 'comment_update'),
    path('comment_delete/<int:comment_id>/', views.comment_delete, name = 'comment_delete'),
    path('hashtag_create/', views.hashtag_create, name = 'hashtag_create'),
]