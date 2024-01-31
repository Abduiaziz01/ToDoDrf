from rest_framework.routers import DefaultRouter

from apps.task.views import TaskAPIViewSet

router = DefaultRouter()
router.register('task', TaskAPIViewSet, 'api_task')


urlpatterns = router.urls 
