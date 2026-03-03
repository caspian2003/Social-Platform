from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
]