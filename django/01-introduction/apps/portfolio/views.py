from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404
import json

from portfolio.models import Project, Client



def project_list(request):
    
    projects = Project.objects.all()
    clients = Client.objects.all()

    data = {
            'projects': projects,
            'clients': clients
            }
    
    return TemplateResponse(request, 'portfolio/project_list.html', data)

def project_detail(request, pk):
    
    project = get_object_or_404(Project, pk=pk)

    data = {
            'project': project
            }
    
    return TemplateResponse(request, 'portfolio/project_detail.html', data)



def comment_list(request, pk):
    
    project = get_object_or_404(Project, pk=pk)
    content = []
    
    for comment in project.comment_set.all():
        c = {
             'username': comment.username,
             'text': comment.text,
             }
        content.append(c)
        
    import time
    time.sleep(1)
    
    return HttpResponse(json.dumps(content), content_type='application/json')

