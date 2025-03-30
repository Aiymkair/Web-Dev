from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

# List all companies and get one company
class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyDetailAPIView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

# List Vacancies for a Company
class CompanyVacanciesAPIView(generics.ListAPIView):
    serializer_class = VacancySerializer

    def get_queryset(self):
        company_id = self.kwargs['id']
        return Vacancy.objects.filter(company_id=company_id)

# List all vacancies and get one vacancy
class VacancyListAPIView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

class VacancyDetailAPIView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

# List top 10 vacancies by salary (descending)
class TopTenVacanciesAPIView(APIView):
    def get(self, request):
        top_vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(top_vacancies, many=True)
        return Response(serializer.data)
