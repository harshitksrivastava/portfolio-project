from django.shortcuts import render

from .models import Project

# Create your views here.
def project(request):
     projects = Project.objects.all()
     return render(request,'jobs/projects.html',{'projects':projects})

def home(request):
    return render(request,'jobs/home.html')


def education(request):
    return render(request,'jobs/education.html')
