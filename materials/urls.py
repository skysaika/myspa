from materials.apps import MaterialsConfig
from rest_framework.routers import DefaultRouter

from .views import CourseViewSet

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register('courses', CourseViewSet, basename='courses')
# router.register('lessons', LessonViewSet)


urlpatterns = [

] + router.urls
