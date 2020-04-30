from django_filters import rest_framework, NumberFilter

from django.http import HttpResponse
import csv
import os
import django

from .models import User, Food, Bookmark, Stats
from rest_framework import viewsets, generics
from .serializers import UserSerializer, FoodSerializer, BookMarkSerializer, StatsSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()  
    serializer_class = UserSerializer 
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('ID', 'UserName', 'PW', 'Age', 'Sex', 'Height', 'Weight', 'ActivityIndex', 'UserKcal', )

class FoodViewSet(viewsets.ModelViewSet):  
    queryset = Food.objects.all()  
    serializer_class = FoodSerializer    
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('Num', 'FoodName', 'Category', 'ServingSize', 'Kcal', 'Carbo', 'Protein', 'Fat', 'Natrium',)


class BookmarkViewSet(viewsets.ModelViewSet):
    queryset = Bookmark.objects.all()  
    serializer_class = BookMarkSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('BMNum', 'user', 'FoodNum', )

class StatsViewSet(viewsets.ModelViewSet):
    queryset = Stats.objects.all()  
    serializer_class = StatsSerializer
    filter_backends = (rest_framework.DjangoFilterBackend, )
    filter_fields = ('StatsID', 'user', 'FoodNum', 'Date', 'Kcal', 'Carbo', 'Protein','Fat','Natrium', )
