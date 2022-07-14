from api.views import CommentViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('api/v1/posts', PostViewSet)
router.register('api/v1/groups', GroupViewSet)
router.register(
    r'api/v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
