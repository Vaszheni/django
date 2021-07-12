from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Bd
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template('shop/index.html')
    books = Bd.objects.order_by('name')
    context = {'books': books}

    return HttpResponse(template.render(context, request))


def products(requsest):
    books = Bd.objects.all()
    response = []
    for book in books:
        response.append(
            {
                "id": book.id,
                "title": book.name,
                "price": book.price
            }
        )
    return JsonResponse(response, safe=False)
