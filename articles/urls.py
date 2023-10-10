from django.urls import path
from .views import list_view, detail_view, create_view, update_view, delete_view, likes_view

urlpatterns = [
    path('', list_view, name='home'),
    path('articles/<int:pk>/', detail_view, name='detail'),
    path('articles/create/', create_view, name='create'),
    path('articles/update/<int:pk>/', update_view, name='update'),
    path('articles/delete/<int:pk>/', delete_view, name='delete'),
    path('articles/likes/<int:pk>/', likes_view, name='like-article'),
   
]