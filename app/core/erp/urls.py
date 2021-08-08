
from django.http import request
from django.urls import path

from core.erp.views import myfristview, secondview





urlpatterns = [
    path('uno/',myfristview,name="vista1"),
    path('dos/',secondview, name='vista2'),

]




