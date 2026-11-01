from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to my home page!")
def about(request):
    return HttpResponse("student portal management system")
def contact(request):
    return HttpResponse("contact the student administration")
def courses(request):
    return HttpResponse("Available Courses:python,Django,java")

def student_details(request,student_id):
    return HttpResponse(f"Student ID:{student_id}")
def student_profile(request,username):
    return HttpResponse(f"student profile:{username}")
def course_details(request,course_name):
    return HttpResponse(f"course Name:{course_name}")
