from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import *
from django.template import loader
# Create your views here.
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.serializers.json import DjangoJSONEncoder
from .serializers import *

def map(request):
    
    if len(arduino.objects.all())==0:
        raise Http404("arduino does not exist")
    arduinos=arduino.objects.all().order_by('-pub_date')
    
    
    context={"arduinos" : arduinos,"js_arduinos" : json.dumps([a.to_json() for a in arduinos], cls=DjangoJSONEncoder)}
    return render(request,"myapp/map.html",context)

class UpdateGPS(APIView):
    def get(self, request, format=None):
        arduinos = arduino.objects.all()
        serializer = ArduinoSerializer(arduinos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        arduino_serializer = ArduinoSerializer(data=request.data)
        if arduino_serializer.is_valid():
            arduino_serializer.save() #UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(arduino_serializer.data, status=status.HTTP_201_CREATED) #client에게 JSON response 전달
        else:
            return Response(arduino_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        