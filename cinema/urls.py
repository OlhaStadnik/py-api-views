from django.urls import path, include
from rest_framework import routers

from cinema.views import MovieViewSet, GenreList, GenreDetail, ActorList, \
    CinemaHallViewSet

cinema_hall_list = CinemaHallViewSet.as_view(
    actions={"get": "list", "post": "create"})
cinema_hall_detail = CinemaHallViewSet.as_view(
    actions={"get": "retrieve",
             "put": "update",
             "patch": "partial_update",
             "delete": "destroy"}
)
router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")
router.register("cinema_halls", CinemaHallViewSet,
                basename="cinema_halls")
urlpatterns = [
    path("", include(router.urls)),
    path("genres/", GenreList.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genre-detail"),
    path("actors/", ActorList.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorList.as_view(), name="actor-detail"),

]

app_name = "cinema"
