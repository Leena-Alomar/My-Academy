from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    course_name=models.CharField(max_length=50)
    course_description=models.TextField(max_length=250)
    course_time= models.CharField(max_length=50)
    class_date=models.CharField(max_length=50)
    teacher=models.OneToOneField('User',on_delete=models.CASCADE)
    
      
    def __str__(self):
        return self.course_name


class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    user_email=models.EmailField(max_length=255, unique=True)
    user_pass=models.CharField(max_length=50)
    user_Fname= models.CharField(max_length=255)
    user_Lname= models.CharField(max_length=255)
    is_teacher=models.BooleanField(default=False)
    enrolled_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='students')

    def __str__(self):
        return self.user_email


class Schedule(models.Model):
    schedule_id=models.AutoField(primary_key=True)
    schedule_name = models.CharField(max_length=50)
    course_related=models.ForeignKey(Course,on_delete=models.CASCADE)

     
    def __str__(self):
        return self.schedule_name

class Lesson(models.Model):
    lesson_id=models.AutoField(primary_key=True)
    lesson_name=models.CharField(max_length=50)
    lesson_time=models.CharField(max_length=50)
    lesson_week=models.CharField(max_length=50)
    lesson_brief=models.TextField()
    lesson_sch=models.ForeignKey(Schedule,on_delete=models.CASCADE ,related_name='lessons')
    
    def __str__(self):
        return self.lesson_name