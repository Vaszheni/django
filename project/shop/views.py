from django.http import HttpResponse
from django.shortcuts import render
from .models import Bd
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('shop/index.html')
    books = Bd.objects.order_by('name')
    context = {'books': books}

    return HttpResponse(template.render(context, request))
