from django.urls import path
from .views import (
    CompaniesListAPIView, CompanyDetailAPIView, CompanyVacanciesAPIView,
    VacancyListAPIView, VacancyDetailAPIView, TopTenVacanciesAPIView
)

urlpatterns = [
    path('companies/', CompaniesListAPIView.as_view(), name='company-list'),
    path('companies/<int:id>/', CompanyDetailAPIView.as_view(), name='company-detail'),
    path('companies/<int:id>/vacancies/', CompanyVacanciesAPIView.as_view(), name='company-vacancies'),
    path('vacancies/', VacancyListAPIView.as_view(), name='vacancy-list'),
    path('vacancies/<int:id>/', VacancyDetailAPIView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', TopTenVacanciesAPIView.as_view(), name='top-ten-vacancies'),
]
