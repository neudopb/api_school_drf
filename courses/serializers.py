from rest_framework import serializers
from django.db.models import Avg
from .models import (
    Course,
    Evaluation,
)


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

    def validate_note(self, value): # def name is "validate_" + field name
        if value in range(1, 6):
            return value

        raise serializers.ValidationError("A nota precisa ser um inteiro entre 1 e 5")

    
class CourseSerializer(serializers.ModelSerializer):
    # Nested Relationship
    evaluations = EvaluationSerializer(many=True, read_only=True)
    
    # Primary Key Related Field
    # evaluations = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # Hyperlinked Related Field
    """
    evaluations = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name="evaluation-detail"
    )
    """
    average_evaluations = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = [
            "id",
            "title",
            "url",
            "created",
            "is_active",
            "evaluations",
            "average_evaluations"
        ]

    def get_average_evaluations(self, obj):
        average = obj.evaluations.aggregate(Avg("note")).get("note__avg")

        if average is None:
            return 0
        return round(average * 2) / 2