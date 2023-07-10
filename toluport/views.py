from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('message.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def memberstitle(request):
  template = loader.get_template('index.html')
  context = {
    'mymembers': 'John',
  }
  return HttpResponse(template.render(context, request))