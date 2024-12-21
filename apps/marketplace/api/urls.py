
from django.urls import path
from . import views

app_name = 'marketplace-api'

urlpatterns = [
    path('', views.SoftwareListView.as_view(), name='list'),
    path('<int:pk>/', views.SoftwareDetailView.as_view(), name='detail'),
]
