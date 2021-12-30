from django.http.response import HttpResponse
from django.shortcuts import render
from.models import Cats,Exams,Notes

# Create your views here.
def index(request):
    return render (request,'index.html')

def exams(request):
    return render (request,'exams.html')

def cats(request):
    return render (request,'cats.html')

def notes(request):
    return render (request,'pdfnotes.html')

def fund(request):
    return render (request,'fund.html')

def catss(request):
    a=request.POST['unitcode']
    b=request.POST['unitname']
    c=request.POST['yeardone']
    d=request.FILES.get('image')
    e=Cats(unitcode=a,unitname=b,yeardone=c,image=d)
    e.save()
    return HttpResponse(" cat uploaded successfully,Thank you !")

def examss(request):
    a=request.POST['unitcode']
    b=request.POST['unitname']
    c=request.POST['yeardone']
    d=request.FILES.get('image')
    e=Exams(unitcode=a,unitname=b,yeardone=c,image=d)
    e.save()
    return HttpResponse(" exam uploaded successfully,Thank you!")

def notess(request):
    a=request.POST['unitcode']
    b=request.POST['unitname']
    d=request.FILES.get('pdf')
    e=Notes(unitcode=a,unitname=b,pdf=d)
    e.save()
    return HttpResponse(" exam uploaded successfully,Thank you!")

def searchcats(request):
    a=request.POST['unitcode']
    b=Cats.objects.get(unitcode=a)
    return render (request,'search.html',{"b":b})

def searchexams(request):
    a=request.POST['unitcode']
    b=Exams.objects.get(unitcode=a)
    return render (request,'search1.html',{"b":b})

def searchnotes(request):
    a=request.POST['unitcode']
    b=Notes.objects.get(unitcode=a)
    return render (request,'search2.html',{"b":b})



    
