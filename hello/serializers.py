from rest_framework import serializers
from .models import User, Food, Bookmark, Stats

class UserSerializer(serializers.ModelSerializer):
    class Meta : 
        model = User
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Food
        fields = '__all__'


class BookMarkSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Bookmark
        fields = '__all__'

class StatsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Stats
        fields = '__all__'