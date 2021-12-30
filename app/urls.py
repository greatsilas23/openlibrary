

from django.urls import path
from.import views

urlpatterns = [
    path('',views.index,name="index"),
    path('cats',views.cats,name="cats"),
    path('exams',views.exams,name="exams"),
    path('notes',views.notes,name="notes"),
    path('fund',views.fund,name="fund"),
    path('catss',views.catss,name="catss"),
    path('examss',views.examss,name="examss"),
    path('notess',views.notess,name="notess"),
    path('searchcats',views.searchcats,name="searchcats"),
    path('searchexams',views.searchexams,name="searchexams"),
    path('searchnotes',views.searchnotes,name="searchnotes"),
    

]


