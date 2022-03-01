from unittest import result
from django.shortcuts import render
from .models import Producer, Province
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProducerSerializer, ProvinceSerializer

# Create your views here.
class ProvinceView(APIView):
    
    def post(self, request):
        result = ProvinceSerializer.create(self,request.data)
        return Response(status=status.HTTP_201_CREATED, data ={"data" :  ProvinceSerializer(result).data})

class ProvinceShortfallView(APIView):
    def get(self,request,province_code):
        result =ProvinceSerializer.get_shortfall(self,province_code)
        return Response(status=status.HTTP_200_OK, data ={"data" :  result})

class ProducerView(APIView):
    def post(self, request):
        result = ProducerSerializer.create(self,request.data)
        return Response(status=status.HTTP_201_CREATED, data ={"data" :  ProducerSerializer(result).data})


class ProducerListView(APIView):
    def get(self, request, province_code):
        province = Province.objects.get(province_code = province_code)
        result = Producer.objects.filter(province_id=province)
        return Response(status=status.HTTP_200_OK, data ={"data" :  ProducerSerializer(result, many=True).data})