from django.shortcuts import render
from .models import Project, Certificate

def project_list(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'index.html', {'projects': projects, 'certificates': certificates})


def message_view(request):
    return render(request, 'message.html')
