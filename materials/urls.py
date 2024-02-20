from django.urls import path

from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')


urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),  # для создания урока
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),  # для создания урока
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-view'),  # для создания урока
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),  # для создания урока
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson-delete'),  # для создания урока
] + router.urls
