from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import ShopList


def index(req):
    return HttpResponse('Index of mylists')

def index_render(req):

    shop_filter = req.GET.get('filter', '')
    mylists = ShopList.objects.filter(shoplist_name__startswith=shop_filter)

    return render(
        request=req,
        template_name='index.html', context={'mylists': mylists}
    )