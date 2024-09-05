from django.shortcuts import render, HttpResponse
from django.http import JsonResponse


from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ItemSerializer
from .models import Item
# Create your views here.


# def item_list(request):
#     # QueryObj -> python list
#     items = Item.objects.all()
#     item_li = []
#     for item in items:
#         item_li.append({
#             'name': item.name,
#             'price': item.price,
#             'description': item.description,
#         })
#     # return HttpResponse(items)
#     return JsonResponse({"menu_items": item_li})

@api_view(['GET'])
def item_list(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)


def item_list_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def item_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializer(item)
    return Response(serializer.data)
