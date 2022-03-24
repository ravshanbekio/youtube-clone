from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, PlaylistViewSet, VideoViewSet, CommentViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('users',UserViewSet)
router.register('playlists',PlaylistViewSet)
router.register('videos',VideoViewSet)
router.register('comments',CommentViewSet)

#Documentation settings
schema_view = get_schema_view(
   openapi.Info(
      title="YouTube API (Clone)",
      default_version='v1',
      description="This is YouTube clone API. \n You may use this API on public!!!",
      contact=openapi.Contact("Ravshanbek Madaminov <ravshanbekmadaminov68@gmail.com> <+998903036415>"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('',include(router.urls)),
    path('documentation/',schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]