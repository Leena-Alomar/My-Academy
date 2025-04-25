from django.contrib import admin
from django.urls import path, include
from .views import .CourseDetailsView,ScheduleDetailsView,ScheduleLessonRelationView ,LessonDetailsView ,LessonRelationView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    path('course/<int:coures_id>/', views.CourseDetailsView.as_view(), name='course-detail'),
    path('schedule/<int:schedule_id>/', views.ScheduleDetailsView.as_view(), name='schedule-detail'),
    path('schedule/<int:schedule_id>/lesson/<int:lesson_id>/', views.ScheduleLessonRelationView.as_view(), name='schedule-lesson-relation'),
    path('lesson/<int:lesson_id>/', views.LessonDetailsView.as_view(), name='lesson-detail'),
    path('schedule/<int:schedule_id>/lesson/<int:lesson_id>/', views.LessonRelationView.as_view(), name='lesson-relation'),
]