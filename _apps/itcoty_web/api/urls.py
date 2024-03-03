from django.urls import include, path

from .views import (AllVacanciesView, GoogleLoginView, UserRedirectView,
                    VacanciesView)

urlpatterns = [
    path("", include("dj_rest_auth.urls")),
    path("registration/", include("dj_rest_auth.registration.urls")),
    path("google/login/", GoogleLoginView.as_view(), name="google_login"),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect"),
    path("get-all-vacancies/", view=AllVacanciesView.as_view(), name="all_vacancies"),
    path("vacancies/", view=VacanciesView.as_view(), name="vacancies"),
]
