from django.contrib import admin
from cursos.models import (
    Course,
    Evaluation,
)


admin.site.register(Course)
admin.site.register(Evaluation)