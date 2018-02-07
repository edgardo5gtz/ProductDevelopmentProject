from django.urls import path
from . import views


urlpatterns = [
    path(r'risks_api/', views.RisksList.as_view()),
    path(r'risks_api/<pk>/', views.RisksDetails.as_view()),
]
