from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),

    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),

    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

    path('post/<int:pk>/likes/', views.likes, name='likes'),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),

]
