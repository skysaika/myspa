from rest_framework import viewsets

from materials.models import Course
from materials.serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """Вьюсет курса."""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
