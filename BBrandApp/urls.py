from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SvgUpdateView, SvgPathListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'), 
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),          
    path('about/', views.about, name='about'),
    path('svg/<int:pk>/list', SvgUpdateView.as_view(), name='svg-update'),
    path('svg/<int:pk>/list', SvgPathListView.as_view(), name='svgpath-list'),
    path('parameters/', views.parameters, name= 'parameters'),
    path('user/', views.user, name='user')
    ]

