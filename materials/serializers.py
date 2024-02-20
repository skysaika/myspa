from rest_framework import serializers

from materials.models import Course


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор курса."""
    class Meta:
        model = Course
        fields = "__all__"
