from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    UserViewSet,
    CategoryViewSet,
    TagViewSet,
    PostViewSet,
    CommentViewSet,
)


router_v1 = DefaultRouter()
router_v1.register('users', UserViewSet)
router_v1.register('categories', CategoryViewSet)
router_v1.register('tags', TagViewSet)
router_v1.register('posts', PostViewSet)
router_v1.register('comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
