from django.urls import path 
from . import views

urlpatterns = [ 
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
    path('no_profile', views.no_profile_view, name='no_profile')
]