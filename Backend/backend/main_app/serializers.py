from rest_framework import serializers
from .models import Course,User,Schedule,Lesson

class UserSerializer(serializers.ModelSerializer):
    user_pass = serializers.CharField(write_only=True) 

    class Meta:
        model = User
        fields = ('user_id', 'user_Fname','user_Lname', 'user_email', 'user_pass')

        


class CourseSerializer(serializers.ModelSerializer):
    teacher =  serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = Course
        fields = '__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    lessons =  LessonSerializer(many=True,read_only=True)
    class Meta:
        model = Schedule
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lesson
        fields = '__all__'