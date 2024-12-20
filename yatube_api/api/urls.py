from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet,
                basename="comment")
router.register("groups", GroupViewSet)
router.register("posts", PostViewSet)
router.register("follow", FollowViewSet, basename="follow")

urlpatterns = [
    path("v1/", include(router.urls)),
    path("v1/", include("djoser.urls")),
    path("v1/", include("djoser.urls.jwt")),
]
