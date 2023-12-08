# num_to_english/serializers.py
from rest_framework import serializers
from .models import Number

class NumberSerializer(serializers.Serializer):
    number = serializers.IntegerField()
