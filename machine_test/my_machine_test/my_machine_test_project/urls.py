from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectViewSet, list_projects_for_user

# Create router and register viewsets for API
router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),  # The API endpoints will be listed under /api/
    path('user/projects/', list_projects_for_user, name='user-projects'),
]
