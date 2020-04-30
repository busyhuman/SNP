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
            Num = row[0],
            FoodName = row[4],
            Category = row[8],
            ServingSize = row[9],
            Kcal = row[11],
            Carbo = row[17],
            Protein = row[15],
            Fat = row[16],
            Natrium = row[38],
        )

"""