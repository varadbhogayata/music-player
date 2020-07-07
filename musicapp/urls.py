from django.urls import path
from . import views

# Add URLConf
urlpatterns = [
    path('', views.index, name='index'),
    path('user-home/', views.user_home, name='user-home'),
]
