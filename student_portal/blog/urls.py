from django.urls import path,re_path
from .import views

urlpatterns=[
    path('',views.home,name='blog_home'),
    path('about/',views.about,name='about'),
    path('latest/',views.latest_posts,name='latest_posts'),
    path('categories/',views.categories,name='categories'),


    path('article/<int:year>/<int:month>/<int:date>/', views.article_details, name='article_details'),
    re_path(r'^year/(?P<year>\d{4})/$',views.article_by_year,name='article_by_year'),
    re_path(r'^month/(?P<month>\d{2})/$',views.article_by_month,name='article_by_month'),
    re_path(r'^archive/(?P<year>\d{4})/$',views.archive,name='archive'),
    path('report/<int:year>/<int:month>/<str:department>/',views.academic_report,name='academic_report'),  
]