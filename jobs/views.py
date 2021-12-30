from django.shortcuts import render, get_object_or_404
from .models import Project

def apurva(request):
    return render(request,'jobs/apurva.html')

def home(request):
    projects = Project.objects
    return render(request,'jobs/home.html',{'projects':projects})

def detail(request, project_id ):
    projects = get_object_or_404(Project, pk = project_id)
    return render(request,'jobs/detail.html',{'projects':projects})
