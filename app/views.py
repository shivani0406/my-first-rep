from django.shortcuts import render,HttpResponse
from .models import Employee                             #import karna padega 

# Create your views here.

# def homepage(request):
#     print(request.method,request.user)                     #optional to check only
#     return HttpResponse("Hello")

# def homepage(request):
#     print(request.method,request.user)                     #optional to check only which method we use and user name from which we logged in
#     return render(request , "home.html")

def homepage(request):
    emps = Employee.objects.all()                              #pehele epl call karna padega  
    return render(request , "home.html",context={"name":["Ant","Bat","Cat","Dog"] ,"all_emp": emps } )                  # to see emp list on html page      #import Employee