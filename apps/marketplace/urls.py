
from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.software_list, name='list'),
    path('<int:pk>/', views.software_detail, name='detail'),
]
