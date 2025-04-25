from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course,User,Schedule,Lesson
from .serializers import UserSerializer,CourseSerializer,ScheduleSerializer ,LessonSerializer
from django.shortcuts import get_object_or_404

# Define the home view
class CoursDetailsView(APIView):

   def get(self, request, course_id):
        course = get_object_or_404(Course, pk=id)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

class ScheduleDetailsView(APIView):

   def get(self, request, id):
        schedule = get_object_or_404(Studio, pk=id)
        serializer = ScheduleSerializer(schedule )
        return Response(serializer.data)

    def delete(self, request, id):
        schedule = get_object_or_404(schdule, pk=id)
        Schedule.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ScheduleLessonRelationView(APIView):
    def put(self, request, schedule_id, lesson_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except (Schedule.DoesNotExist, Lesson.DoesNotExist):
            return Response({'error': 'Schedule or Lesson not found'}, status=404)
        schedule.lesson.add(lesson)
        return Response({'message': f'Lesson {Lesson.leeson_name} added to Schedule {Schedule.Schedule_id}'}, status=200)

    def delete(self, request, schedule_id, lesson_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except (Schedule.DoesNotExist, Lesson.DoesNotExist):
            return Response({'error': 'Schedule or Lesson not found'}, status=404)
        schedule.lesson.remove(lesson)
        return Response({'message': f'Lesson {Lesson.leeson_name} added to Schedule {Schedule.Schedule_id}'}, status=200)

    def post(self, request, schedule_id, lesson_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except (Schedule.DoesNotExist, Lesson.DoesNotExist):
            return Response({'error': 'Schedule or Lesson not found'}, status=404)
        schedule.lesson.save(lesson)
        return Response({'message': f'Lesson {Lesson.leeson_name} added to Schedule {Schedule.Schedule_id}'}, status=200)


class LessonDetailsView(APIView):

   def get(self, request, id):
        lesson = get_object_or_404(Lesson, pk=id)
        serializer = LessonSerializer(lesson )
        return Response(serializer.data)

    def delete(self, request, id):
        lesson = get_object_or_404(Lesson, pk=id)
        Lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LessonRelationView(APIView):
    def put(self, request, lesson_id):
        try:
            lesson = Lesson.objects.get(id=Lesson_id)
        except ( Lesson.DoesNotExist):
            return Response({'error': ' Lesson not found'}, status=404)
        schedule.lesson.add(lesson)
        return Response({'message': f'Lesson {Lesson.leeson_name} has been added '}, status=200)

    def delete(self, request, lesson_id):
        try:
            lesson = Lesson.objects.get(id=lesson_id)
                if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request,lesson_id):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)