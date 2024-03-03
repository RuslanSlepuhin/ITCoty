from django.contrib import admin

from .models import AdminVacancies, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
    )


@admin.register(AdminVacancies)
class AVacanciesAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "vacancy_url",
        "company",
        "salary",
        "time_of_public",
        "created_at",
        "agregator_link",
    )
    list_display_links = ("id", "title")
