from django.urls import path
from .views import (
    CoursesAPIView,
    CourseAPIView,
    EvaluationsAPIView,
    EvaluationAPIView,
)


urlpatterns = [
    path("courses/", CoursesAPIView.as_view(), name="courses"),
    path("courses/<int:pk>/", CourseAPIView.as_view(), name="course"),
    path("evaluations/", EvaluationsAPIView.as_view(), name="evaluations"),
    path("evaluations/<int:pk>/", EvaluationAPIView.as_view(), name="evaluation")
]