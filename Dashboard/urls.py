from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard),
    path('AddEntry', views.Addentry),
    path('Analytics', views.Analytics),
]
