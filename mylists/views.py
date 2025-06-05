from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ShopList


def index(req):
    return HttpResponse('Index of mylists')

def index_render(req):

    mylists = ShopList.objects.all()
    return render(
        request=req,
        template_name='index.html', context={'mylists': mylists}
    )