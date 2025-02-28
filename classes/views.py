from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,"home.html")
def greet(request,name="default"):
    context= {
        "name":name,
        "description":"Hello "
    }
    return render(request,"greet.html",context )
def class_area(request):
    height = request.GET.get('height',0)
    width = request.GET.get('width',0)
    height = float(height) if height else None
    width = float(width) if width else None
    area = height * width if height and width else None
    context = {
        "height": height,
        "width": width,
        "area": area
    }
    return render(request, "class_area.html", context)