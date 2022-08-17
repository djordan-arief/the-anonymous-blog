from django.urls import path
from user_app import views


urlpatterns = [
    path('profile/', views.profilepage, name='profile-page'), 
    path('contact/', views.contactpage, name='contact-page'),

]