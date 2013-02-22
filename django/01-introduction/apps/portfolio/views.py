from django.http import HttpResponse
from django.template.response import TemplateResponse

from portfolio.models import Project, Client

def project_list(request):
    
    projects = Project.objects.all()
    clients = Client.objects.all()

    data = {
            'projects': projects,
            'clients': clients
            }
    
    return TemplateResponse(request, 'portfolio/project_list.html', data)
