from rest_framework import generics
from rest_framework.permissions import AllowAny

from ..models import AdminVacancies
from ..serializers import AllVacanciesSerializer


class AllVacanciesView(generics.ListAPIView):
    queryset = AdminVacancies.objects.all()
    serializer_class = AllVacanciesSerializer
    permission_classes = [AllowAny]
