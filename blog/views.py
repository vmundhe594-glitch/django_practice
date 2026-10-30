from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("welcome to the Blog")

def about(request):
    return HttpResponse("About our blog")

def latest_posts(request):
    return HttpResponse("Display Latest Blog posts")

def categories(request):
    return HttpResponse("Available Blog categories")

def article_details(request, year, month,date):
    return HttpResponse(f"Articles from {year} - {month}-{date}")

def article_by_year(request,year):
    return HttpResponse(f"Articles published in{year}")

def article_by_month(request,month):
    return HttpResponse(f"Articles published in{month}")

def academic_report(request,**kwargs):
    year=kwargs.get('year')
    month=kwargs.get('month')
    department=kwargs.get('department')

    return HttpResponse(f"Academic Report<br>"
                        f"year:{year}<br>"
                        f"month:{month}<br>"
                        f"department:{department}")

def archive(request,year):
    return HttpResponse(f"year:{year}")