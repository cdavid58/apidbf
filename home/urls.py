from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^GetInventory/$',GetInventory,name="GetInventory"),		
		url(r'^SetInventory/$',SetInventory,name="SetInventory"),		
]