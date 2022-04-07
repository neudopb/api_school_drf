from rest_framework import serializers
from .models import (
    Course,
    Evaluation,
)


class CourseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "url",
            "created",
            "is_active",
        ]


class EvaluationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evaluation
        fields = [
            "id",
            "course",
            "name",
            "email",
            "comment",
            "note",
            "created",
            "is_active",
        ]
        extra_kwargs = {
            "email": {"write_only": True},
        }