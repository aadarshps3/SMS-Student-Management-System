from django.urls import path

from SMS_app import views

urlpatterns=[
    path('',views.Index,name="Index"),
    path('loginpage',views.loginpage,name="loginpage"),
    path('teacher_reg',views.teacher_reg,name="teacher_reg"),
    path('student_reg',views.student_reg,name="student_reg"),
    path('teacherpage',views.teacherpage,name="teacherpage"),
    path('studentpage',views.studentpage,name="studentpage"),
]