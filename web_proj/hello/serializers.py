from rest_framework import serializers
from .models import User, Food, Bookmark, Stats
from django import forms

class UserSerializer(serializers.ModelSerializer):
    PW = forms.CharField(widget=forms.PasswordInput)
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