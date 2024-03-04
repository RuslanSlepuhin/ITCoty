from datetime import date, timedelta

from django_filters import rest_framework as filters
from rest_framework import generics, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny

from ..filters import VacancyFilter
from ..models import AdminVacancy, Vacancy
from ..serializers import AllVacanciesSerializer, VacanciesSerializer


class AllVacanciesView(generics.ListAPIView):
    queryset = AdminVacancy.objects.all()
    serializer_class = AllVacanciesSerializer
    permission_classes = [AllowAny]


class VacanciesViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    date_start = date.today() - timedelta(days=20)
    queryset = (
        Vacancy.objects.filter(created_at__gt=date_start).order_by("-id")
        # .distinct("id", "body") use in postgres only
    )
    serializer_class = VacanciesSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = VacancyFilter
    pagination_class = LimitOffsetPagination
