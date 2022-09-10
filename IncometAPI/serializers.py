from IncometAPI.models import *
from rest_framework import serializers
# from Auth.serializers import UserUpdateSerializer
from Auth.models import *

# class UserUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = (
#             'salutation', 'first_name', 'last_name', 'about', 'avatar',
#             'cover_picture', 'skills', 'address', 'enlarge_url', 'date_of_birth',venv
#             'birth_place', 'gender'
#         )

class DescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptions
        fields = '__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'        


class CoursesSerializer(serializers.ModelSerializer):
    # cources_get=serializers.SerializersMethodField()
    rating_number = serializers.SerializerMethodField()
    # cources_get=serializers.SerializersMethodField()
    buy_cources_user = serializers.SerializerMethodField()
    class Meta:
        model = Courses
        fields = ['id','courses_name','courses_discriptions','courses_start_date','courses_end_date','courses_pdf','courses_price','created_date','update_date','is_active','is_verify','rating_number','buy_cources_user'] 



    def get_rating_number(self, obj):
        rating = Rating.objects.filter(courses=obj).values()
        return rating  

    def get_buy_cources_user(self, obj):
        by_courses = ByCourses.objects.filter(courses=obj).values()
        return by_courses



    
class RatingSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(read_only=True)
    class Meta:
        model = Rating
        fields = '__all__' 


# class ByCoursesUserSerializer(serializers.ModelSerializer):
#     userdata_buy=serializers.SerializersMethodField()
#     class Meta:
#         model = ByCourses
#         fields=['id','userdata_buy']

#     def get_userdata_buy(self, obj):
#         use = Courses.objects.filter(courses=obj,user=obj).values()
#         return use  



class ByCoursesSerializer(serializers.ModelSerializer):
    courses = CoursesSerializer(read_only=True)
    
    class Meta:
        model = ByCourses
  
        fields='__all__'



# class ByCoursesSerializer1(serializers.ModelSerializer):
#     # courses = CoursesSerializer(read_only=True)
#     userdata_buy=serializers.SerializersMethodField()
#     class Meta:
#         model = ByCourses
#         fields=['id', 'userdata_buy']
#     def get_userdata_buy(self, obj):
#         use = Courses.objects.filter(courses=obj)
#         return use  

        





    


    

        

