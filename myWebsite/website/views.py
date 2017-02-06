from django.shortcuts import render, render_to_response
from django.conf import settings
from .models import *
from django.http import HttpResponseRedirect, HttpResponse


# Create your views here.
def index(request):
        list_of_project = projects.objects.all()
        for i in list_of_project:
            list_of_description = i.description.split('*')
            i.description = list_of_description[1:]

        
            
        author = myself.objects.all()
        author = author[0]
        list_of_myself_description = author.description.split('\n')
        author.description = list_of_myself_description
        return render_to_response('index.html', {'object': list_of_project,\
                                                 'myself': author})
        










        
