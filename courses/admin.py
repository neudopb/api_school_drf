from django.contrib import admin
from .models import (
    Course,
    Evaluation,
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "url",
        "created",
        "updated",
        "is_active",
    )
    search_fields = (
        "title",
        "url",
    )
    list_filter = (
        "is_active",
    )

@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "name",
        "email",
        "note",
        "created",
        "updated",
        "is_active",
    )
    search_fields = (
        "course__title",
        "name",
        "email",
    )
    list_filter = (
        "course__title",
        "email",
        "is_active",
    )