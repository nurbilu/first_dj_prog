from django.shortcuts import render

from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import serializers
from base.models import Product

# @api_view(['GET'])
# def index(req):
#     return render(req, 'home.html')

# @api_view(['GET'])
# def about(req):
#     return render(req, 'about.html')

# @api_view(['GET'])
# def books(req):
#     return render(req, '/books.html')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


@api_view(['GET','POST','DELETE','PUT'])
def products(req):
    id = int(req.GET.get('id', -1))
    all_prd = ProductSerializer(Product.objects.all(), many=True).data
    if req.method == 'GET':
        if int(id > -1):
            temp_prd = Product.objects.get(id=id) 
            single_prd = ProductSerializer(temp_prd, many=false).data
            if req.single_prd == 'true':
                return Response(single_prd)
        return Response(all_prd)
    
    elif req.method == 'POST':
        serializer = ProductSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    elif req.method == 'DELETE':
        temp_prd = Product.objects.get(id=id)
        temp_prd.delete()
        return Response(status=204)
    
    elif req.method == 'PUT':
        temp_prd = Product.objects.get(id=id)
        serializer = ProductSerializer(temp_prd, data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)



