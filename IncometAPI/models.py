from turtle import title
from django.db import models
from Auth.models import User

# Create your models here.

# class Video(models.Model):
#     name = models.FileField(upload_to='images/',null=True)

# class Docs(models.Model):
#     docs = models.FileField(upload_to='images/',null=True)    

# class TeacherProfile(models.Model):
#     name=models.CharField(max_length=200,null=True)
#     image = models.ImageField(upload_to='images/', null=True, blank=True)
#     education_degree=models.CharField(max_length=200,null=True)
#     institute=models.CharField(max_length=200,null=True)
#     experience=models.CharField(max_length=200,null=True)
#     address=models.CharField(max_length=200,null=True)
#     no_of_classes=models.IntegerField()
#     address=models.CharField(max_length=200,null=True)
#     coverase=models.BooleanField()  
#     video = models.ForeignKey(Video,null=True, on_delete=models.CASCADE)
#     docs = models.ForeignKey(Video,null=True, on_delete=models.CASCADE)


class News(models.Model):
    subtitel=models.CharField(max_length=200,null=True)
    source_url=models.URLField( max_length=1000,null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)   
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)

    def __str__(self):
        return self.subtitel


class Descriptions(models.Model):
    title=models.CharField(max_length=200, null=True)
    file=models.ForeignKey(News, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    discriptions=models.CharField(max_length=2000, null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.title


class Courses(models.Model):
    courses_name=models.CharField(max_length=200, null=True)
    courses_discriptions=models.CharField(max_length=800, null=True)
    courses_start_date=models.CharField(max_length=200, null=True)
    courses_end_date=models.CharField(max_length=200, null=True)
    courses_pdf=models.FileField(upload_to='images/', null=True, blank=True)
    courses_price=models.FloatField(null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)
    is_verify = models.BooleanField(default=True)
    rating_number=models.IntegerField(null=True)
    number_of_user=models.IntegerField(null=True)
    def __str__(self): 
        return self.courses_name

class Rating(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="courses")
    courses_rating=models.IntegerField(null=True)
    review=models.CharField(max_length=200,null=True)
    created_date= models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.review



class ByCourses(models.Model):
    user=user=models.ForeignKey(User, on_delete=models.CASCADE)
    courses=models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="courses1")
    created_date= models.DateTimeField(auto_now_add=True, null=True)
    update_date= models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    







    





    






