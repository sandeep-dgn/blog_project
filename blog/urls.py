from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.homepage, name='homepage'),  # Homepage URL
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detail page URL
]
