from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse('Index of mylists')

def index_render(req):
    return render(
        request=req,
        template_name='index.html'
    )