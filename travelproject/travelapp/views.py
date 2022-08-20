from django.shortcuts import render
from . models import travel
from . models import members

def index(request):

    obj=travel.objects.all()
    obj1=members.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
