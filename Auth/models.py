from statistics import mode
from xmlrpc.client import Boolean
from django.db import models
from django.contrib.auth.models import AbstractUser
from Core.models import SoftDeleteModel

BaseModel = None

class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, max_length=250)
    salutation = models.CharField(max_length=30, null=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    about = models.TextField(null=True)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    cover_picture = models.ImageField(upload_to='coverPicture/', null=True, blank=True)
    posts_count = models.IntegerField(null=True, blank=True)
    followers_count = models.IntegerField(null=True, blank=True)
    following_count = models.IntegerField(null=True, blank=True)
    skills = models.TextField(null=True)
    address = models.TextField(null=True)
    enlarge_url = models.URLField(null=True)
    date_of_birth = models.DateTimeField(auto_now_add=False, null=True)
    birth_place = models.CharField(max_length=500, null=True)
    gender = models.CharField(max_length=20, null=True)
    is_mail_verified = models.BooleanField(default=False)
    verify_mail_code = models.TextField(max_length=30, null=True, blank=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'User'

class Admin_user(models.Model):
    email=models.EmailField(max_length=254, null=True)
    password=models.CharField(max_length=200, null=True)
    is_active=models.BooleanField()

    def __str__(self):
        return self.email


class Batch(SoftDeleteModel):
    name = models.CharField(max_length=200, unique=True)
    created_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class GroupUser(SoftDeleteModel):
    group = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, unique=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.group

class ChatMessage(SoftDeleteModel):
    group = models.ForeignKey(Batch, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user

class City(SoftDeleteModel):
    city_name = models.CharField(max_length=200)
    city_code = models.CharField(max_length=20)

    def __str__(self):
        return self.city_name

    class Meta:
        verbose_name_plural = 'Cities'
        db_table = 'city'


class WorkPlace(SoftDeleteModel):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    working_from = models.DateTimeField(auto_now_add=False)
    working_till = models.DateTimeField(auto_now_add=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Work Places'
        db_table = 'work_place'


class Education(SoftDeleteModel):
    school_college_name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    session_from = models.DateTimeField(auto_now_add=False, null=True)
    session_to = models.DateTimeField(auto_now_add=False, null=True)
    attended_for = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.school_college_name

    class Meta:
        verbose_name_plural = 'Education'


class MyPlaces(SoftDeleteModel):
    place_name = models.CharField(max_length=200)
    lat_long = models.CharField(max_length=200, null=True)
    from_date = models.DateTimeField(auto_now_add=False, null=True)
    to_date = models.DateTimeField(auto_now_add=False, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name_plural = 'My Places'
        db_table = 'place'


class SocialLinks(SoftDeleteModel):
    name = models.CharField(max_length=200)
    # unique_id = models.CharField(max_length=100, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social Links'
        db_table = 'social_links'


class MyLanguage(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    read = models.CharField(max_length=200, null=True)
    write = models.CharField(max_length=200, null=True)
    speak = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Languages'
        db_table = 'language'


class MyProjects(SoftDeleteModel):
    project_title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    skills = models.TextField(null=True)
    start_date = models.DateTimeField(auto_now_add=False)
    end_date = models.DateTimeField(auto_now_add=False)
    team_size = models.IntegerField(null=True)
    client_name = models.CharField(max_length=200, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_title

    class Meta:
        verbose_name_plural = 'My Projects'


class MyInterest(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    interest_code = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.interest_code

    class Meta:
        verbose_name_plural = 'My Interest'
        db_table = 'interest'


class MySkills(SoftDeleteModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    skill = models.CharField(max_length=250)


class Followers(SoftDeleteModel):
    following = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='following')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    is_confirmed = models.BooleanField(default=False)


class Interests(models.Model):
    interest = models.CharField(max_length=30)


class Skills(models.Model):
    skill = models.CharField(max_length=30)


class Languages(models.Model):
    language = models.CharField(max_length=30)


class Event(models.Model):
    name=models.CharField(max_length=100, null=True, unique=True)
    date= models.DateTimeField(max_length=100, null=True)
    time =models.CharField(max_length=100, null=True)
    is_active =models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name



class Trainer(models.Model):
    trainer_name=models.CharField(max_length=100, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    trand_by=models.ForeignKey(Languages, on_delete=models.CASCADE, null=True)
    email=models.EmailField(max_length=100, null=True)
    is_active=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name

class Meteril(models.Model):
    trainer_name=models.CharField(max_length=100, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    trand_by=models.ForeignKey(Languages, on_delete=models.CASCADE, null=True)
    email=models.EmailField(max_length=100, null=True)
    is_active=models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return self.name






