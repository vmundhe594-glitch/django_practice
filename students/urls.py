from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='student_home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('courses/',views.courses,name='courses'),


    path('details/<int:student_id>/',views.student_details,name='student_details'),
    path('profile/<str:username>/',views.student_profile,name='student_profile'),
    path('course/<str:course_name>/',views.course_details,name='course_details'),
]