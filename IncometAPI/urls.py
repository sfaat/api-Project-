from django.urls import path, include
from IncometAPI.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'News',News1,basename="News")
router.register(r'Newsdetail',Newsdetail,basename="Newsdetail")
router.register(r'CoursesList',CoursesList,basename="CoursesList")
router.register(r'RatingList',RatingList,basename="RatingList")
router.register(r'BuyCoursesList',ByCoursesList,basename="BuyCoursesList")






urlpatterns = [
    path('', include(router.urls))
]
