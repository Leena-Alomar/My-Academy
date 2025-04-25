from django.contrib import admin
from .models import Course,User,Schedule,Lesson

# Register your models here.
admin.site.register(Course)
admin.site.register(User)
admin.site.register(Schedule)
admin.site.register(Lesson)