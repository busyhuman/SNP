"""
import csv
import os
import django
from .models import Food

os.environ.setdefault("DJANGO_SETTING_MODULE", "[web_proj].settings")
django.setup()

CSV_PATH = '/Users/busyh/foods.csv'
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
"""