from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import (
    Course,
    Evaluation,
)
from .serializers import (
    CourseSerializer,
    EvaluationSerializer,
)


"""
API V1
"""


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

    def get_queryset(self):
        if self.kwargs.get("course_pk"):
            return self.queryset.filter(course=self.kwargs.get("course_pk"))
        return self.queryset.all()


class EvaluationAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update and Destroy Evaluation API
    """
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get("course_pk"):
            return get_object_or_404(
                self.get_queryset(),
                course=self.kwargs.get("course_pk"),
                pk=self.kwargs.get("evaluation_pk")
            )
            
        return get_object_or_404(
            self.get_queryset(), 
            pk=self.kwargs.get("evaluation_pk")
        )


"""
API V2
"""


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=["GET"])
    def evaluations(self, request, pk=None):
        self.pagination_class.page_size = 1
        evaluations = Evaluation.objects.filter(course_id=pk)
        page = self.paginate_queryset(evaluations)

        if page is not None:
            serializer = EvaluationSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
            
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer