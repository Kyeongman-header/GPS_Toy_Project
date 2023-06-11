from rest_framework import serializers
from .models import *

class ArduinoSerializer(serializers.ModelSerializer) :
    class Meta :
        model = arduino        # product 모델 사용
        fields = '__all__'