import re
from urllib import response
from django.shortcuts import render
from pandas import notnull
from rest_framework import viewsets, permissions
from rest_framework.permissions import BasePermission
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
# from rest_framework.mixins import 
from IncometAPI.models import *
from rest_framework import viewsets
from IncometAPI.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from Auth.models import User



class Newsdetail(ModelViewSet):
    queryset = Descriptions.objects.all()
    serializer_class = DescriptionsSerializer
    permission_classes = (IsAuthenticated,)    
    



class News1(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = FileSerializer
    permission_classes = (IsAuthenticated,)    


class CoursesList(ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permission_classes = (IsAuthenticated,)  


# class CoursesList(generics.ListAPIView):
#     serializer_class = CoursesSerializer

#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         rating = self.request.rating
#         return Rating.objects.filter(rating=rating)

# class CoursesList(ModelViewSet):
    
#     queryset = Courses.objects.all()
#     serializer_class = CoursesSerializer
    
#     permission_classes = (IsAuthenticated,)      
    

class RatingList(ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)



class ByCoursesList(ModelViewSet):
    queryset=ByCourses.objects.all()
    serializer_class = ByCoursesSerializer
    permission_classes = (IsAuthenticated,)   
    def get_queryset(self, **kwargs):
        user=User.objects.get(id=self.kwargs.get('pk'))
        queryset =ByCourses.objects.filter(user=user, is_active=True)
        return  queryset
       

    

    


    