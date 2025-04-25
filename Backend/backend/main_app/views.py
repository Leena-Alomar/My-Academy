from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course,User,Schedule,Lesson
from .serializers import UserSerializer,CourseSerializer,ScheduleSerializer ,LessonSerializer
from django.shortcuts import get_object_or_404

# Define the Coures view
class CourseDetailsView(APIView):

   def get(self, request):
    try:
      queryset = Course.objects.all()
      serializer = CourseSerializer(queryset, many=True)
      return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as err:
      return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Define the Schedule view
class ScheduleDetailsView(APIView):

    def get(self, request, schedule_id):
def get(self, request, schedule_id):
    try:
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        lessons = Lesson.objects.filter(lesson_sch=schedule)
        return Response({
            "schedule": ScheduleSerializer(schedule).data,
            "lessons": LessonSerializer(lessons, many=True).data,
        }, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def delete(self, request, schedule_id):
    try:
        schedule = get_object_or_404(Schedule, pk=schedule_id)
        schedule.delete()
        return Response({'success': True}, status=status.HTTP_200_OK)
    except Exception as err:
        return Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class ScheduleLessonRelationView(APIView):
    def put(self, request, schedule_id, lesson_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except (Schedule.DoesNotExist, Lesson.DoesNotExist):
            return Response({'error': 'Schedule or Lesson not found'}, status=404)
        lesson.lesson_sch = schedule
        lesson.save()
        return Response({'message': f'Lesson {lesson.lesson_name} added to Schedule {schedule.schedule_id}'}, status=200)

    def delete(self, request, schedule_id, lesson_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
            lesson = Lesson.objects.get(id=lesson_id)
        except (Schedule.DoesNotExist, Lesson.DoesNotExist):
            return Response({'error': 'Schedule or Lesson not found'}, status=404)
        lesson.delete()
        return Response({'message': f'Lesson {lesson.lesson_name} is deleted'}, status=200)

    def post(self, request, schedule_id):
        try:
            schedule = Schedule.objects.get(id=schedule_id)
        except (Schedule.DoesNotExist):
            return Response({'error': 'Schedule not found'}, status=404)

        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(lesson_sch=schedule)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Define the Lesson view
class LessonDetailsView(APIView):
    def get(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        serializer = LessonSerializer(lesson)
        return Response(serializer.data)


    def delete(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, pk=lesson_id)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class LessonRelationView(APIView):
    def put(self, request, lesson_id):
        try:
            lesson = get_object_or_404(Lesson, id=lesson_id)
            serializer = LessonSerializer(lesson, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Lesson.DoesNotExist:
            return Response({'error': 'Lesson not found'}, status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, lesson_id):
        try:

            lesson = Lesson.objects.get(id=lesson_id)
        except ( Lesson.DoesNotExist):
            return Response({'error': ' Lesson not found'}, status=404)
        lesson.lesson_sch = None
        lesson.save()
        lesson.delete()
        return Response({'message': f'Lesson {lesson.lesson_name} is deleted'}, status=200)



    def post(self, request,lesson_id):
        serializer = LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    