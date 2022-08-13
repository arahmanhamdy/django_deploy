from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('users', views.UserApi, basename="users")
router.register('', views.StudentApi, basename="users")

urlpatterns = router.urls

