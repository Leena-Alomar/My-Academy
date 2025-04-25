from rest_framework import serializers
from .models import Course,User,Schedule,Lesson

class UserSerializer(serializers.ModelSerializer):
    user_pass = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ('user_id', 'user_Fname','user_Lname', 'user_email', 'user_pass')


class CourseSerializer(serializers.ModelSerializer):
    teacher =  serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Schedule
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    lessons =  ScheduleSerializer(many=True,read_only=True)
    class Meta:
        model = Lesson
        fields = '__all__'