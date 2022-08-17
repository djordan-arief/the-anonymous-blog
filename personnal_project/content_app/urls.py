from django.urls import path
from . import views
urlpatterns = [
    path('', views.PostListView.as_view(), name='home-page'),
    path('create-content/', views.PostCreateView.as_view(), name='create-content'),
]