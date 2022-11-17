from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from .models import *

@api_view(['POST'])
def GetInventory(request):
	data = request.data
	inventory = Inventory.objects.filter(download=False)
	data = [
		{
			'code': i.code,
			'name': i.name,
			'category': i.category,
			'price_1': i.price_1,
			'price_2': i.price_2,
			'price_3': i.price_3,
			'price_4': i.price_4,
		}
		for i in inventory
	]

	for i in inventory:
		i.download = True
		i.save()

	return Response(data)


@api_view(['POST'])
def SetInventory(request):
	data = request.data
	message= False
	try:
		Inventory(
			code = data['code'],
			name = data['name'],
			category = data['category'],
			price_1 = data['price_1'],
			price_2 = data['price_2'],
			price_3 = data['price_3'],
			price_4 = data['price_4'],
		).save()	
		message = True
	except Exception as e:
		print(e)

	return Response({'Message':message})
	


