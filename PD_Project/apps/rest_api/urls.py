from django.urls import path
from . import views


urlpatterns = [
    path('risks_api/risks/', views.RiskList.as_view()),
    path('risks_api/risk_types/', views.RiskTypeList.as_view()),
    path('risks_api/risk_fields/', views.RiskFieldList.as_view()),
    path('risks_api/text_fields/', views.TextFieldList.as_view()),
    path('risks_api/date_fields/', views.DateFieldList.as_view()),
    path('risks_api/enum_fields/', views.EnumFieldList.as_view()),
    path('risks_api/number_fields/', views.NumberFieldList.as_view()),
    path('risks_api/risks/<pk>/', views.RiskDetails.as_view()),
    path('risks_api/risk_types/<pk>/', views.RiskTypeDetails.as_view()),
    path('risks_api/risk_fields/<pk>/', views.RiskFieldDetails.as_view()),
    path('risks_api/text_fields/<pk>', views.TextFieldDetails.as_view()),
    path('risks_api/date_fields/<pk>', views.DateFieldDetails.as_view()),
    path('risks_api/enum_fields/<pk>', views.EnumFieldDetails.as_view()),
    path('risks_api/number_fields/<pk>', views.NumberFieldDetails.as_view())
]
