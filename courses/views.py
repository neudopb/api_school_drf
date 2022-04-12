from rest_framework import generics
from .models import (
    Course,
    Evaluation,
)
from .serializers import (
    CourseSerializer,
    EvaluationSerializer,
)


class CoursesAPIView(generics.ListCreateAPIView):
    """
    List and Create Course API
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy Course API
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    
class EvaluationsAPIView(generics.ListCreateAPIView):
    """
    List and Create Evaluation API
    """
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy Evaluation API
    """
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer