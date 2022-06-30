from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from product.models import Product
# Create your views here.
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.serializers import ProductSerializer

@api_view(['GET','POST'])
def apihome(request):
    instance =Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        data   = ProductSerializer(instance).data
    return Response(data) 