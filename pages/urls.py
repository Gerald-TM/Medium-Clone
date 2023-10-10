from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('articles.urls')),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('membership/', views.membership_page, name='membership'),
    path('terms/', views.terms_page, name='terms'),
    path('privacy/', views.privacy_page, name='privacy'),
    path('help/', views.help_page, name='help'),
    path('follows/<int:pk>', views.following, name='follows'),
    path('followers/<int:pk>', views.followers, name='followers'),

   
]