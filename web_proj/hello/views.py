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

class FoodViewSet(viewsets.ReadOnlyModelViewSet):
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
    filter_fields = ('StatsID', 'user', 'FoodName', 'Date', 'Kcal', 'Carbo', 'Protein','Fat','Natrium', 'Timeslot', )


def InsertFoodDataIntoFoodTable(request):
    os.environ.setdefault("DJANGO_SETTING_MODULE", "[web_proj].settings")
    django.setup()

    CSV_PATH = './hello/fooddata/foods.csv'
    with open(CSV_PATH, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            Food.objects.create(
                Num = row['Num'],
                FoodName = row['FoodName'],
                Category = row['Category'],
                ServingSize = row['ServingSize'],
                Kcal = row['Kcal'],
                Carbo = row['Carbo'],
                Protein = row['Protein'],
                Fat = row['Fat'],
                Natrium = row['Natrium'],
            )
    
    return HttpResponse("Complete !!")
