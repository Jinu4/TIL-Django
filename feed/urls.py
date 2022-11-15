from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    path('', views.PostView.as_view(), name='homepage'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('new_post/', views.CreatePostView.as_view(), name='new_post'),
]
