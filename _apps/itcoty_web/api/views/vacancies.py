from datetime import date, timedelta

from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..models import AdminVacancy, Vacancy
from ..serializers import AllVacanciesSerializer, VacanciesSerializer


class AllVacanciesView(generics.ListAPIView):
    queryset = AdminVacancy.objects.all()
    serializer_class = AllVacanciesSerializer
    permission_classes = [AllowAny]


class VacanciesView(generics.ListAPIView, generics.RetrieveAPIView):
    date_start = date.today() - timedelta(days=20)
    queryset = (
        Vacancy.objects.filter(created_at__gt=date_start)
        .order_by("-id")
        .distinct("id", "body")
    )
    serializer_class = VacanciesSerializer
    permission_classes = [AllowAny]
