from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, LessonCreateAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')



urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),  # для создания урока
] + router.urls
