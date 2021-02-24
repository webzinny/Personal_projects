from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('delete',delete),
    #path('upload',upload),
    #path('notebook',notebook),
    path('img',image,name='image'),
#registration pages-------------------------------------------------------------------------------------
    path('school',school_registration,name='school'),
    path('teacher/registration',teacher_registration,name='teacher/registration'),
    path('student/registration',student_registration,name='student/regisration'),
#discussionpanel-------------------------------------------------------------------------------------
    path('discussion',discussionpanel,name='discussionpanel'),
    path('tech_discussion',tech_discussionpanel,name='tech_discussionpanel'),
#-------------------------------------------------------------------------------------
    path('student',student,name='student'),
    path('student/notebook',student_notebook,name='student/notebook'),
    path('student/homework',student_homework,name='student/homework'),
    path('student/homeWork/addhomework',student_addhomework,name='student/homework/addhomework'),
#-------------------------------------------------------------------------------------------------
    path('student/homework/english',student_homework_english,name='student/homework/english'),
    path('student/homework/hindi',student_homework_hindi,name='student/homework/hindi'),
    path('student/homework/math',student_homework_math,name='student/homework/math'),
    path('student/homework/science',student_homework_science,name='student/homework/science'),
    path('student/homework/social_science',student_homework_social_science,name='student/homework/social_science'),
#------------------------------------------------------------------------------------------------------------------

    path('student/notes',student_notes,name='student/notes'),
    path('student/notes/english',student_notes_english,name='student/notes/english'),
    path('student/notes/hindi',student_notes_hindi,name='student/notes/hindi'),
    path('student/notes/math',student_notes_math,name='student/notes/math'),
    path('student/notes/science',student_notes_science,name='student/notes/science'),
    path('student/notes/social_science',student_notes_social_science,name='student/notes/social_science'),
#----------------------------------------------------------------------------------------------------------------------
    path('student/lectures',student_lectures,name='student/lectures'),
    path('student/event',student_event,name='student/event'),
#-------------------------------------------------------------------------------------
    path('teacher',teacher,name='teacher'),
    path('teacher/homework',teacher_homework,name='teacher/homework'),
    path('teacher/homework/post',teacher_post_hw,name='teacher/homework/post'),
    path('teacher/homework/posted',teacher_posted_hw,name='teacher/homework/posted'),
    path('teacher/notes',teacher_notes,name='teacher/notes'),
    path('teacher/notes/post',teacher_post_notes,name='teacher/notes/post'),
    path('teacher/notice',teacher_notice,name='teacher/notice'),
    path('teacher/lectures',teacher_lectures,name='teacher/lectures'),
    path('teacher/event',teacher_event,name='teacher/event'),

#-------------------------------------------------------------------------------------
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
