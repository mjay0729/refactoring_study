from django.shortcuts import render
from .models import Producer, Province
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProducerSerializer, ProvinceSerializer

# Create your views here.
class ProvinceView(APIView):
    
    def post(self, request):
        province = ProvinceSerializer.create(self,request.data)
        return Response(status=status.HTTP_201_CREATED, data ={"data" :  ProvinceSerializer(province).data})


class ProducerView(APIView):
    def post(self, request):
        ProducerSerializer.create(self,request.data)
        return Response(status=status.HTTP_201_CREATED)


class ProducerListView(APIView):
    def get(self, request, province_code):
        province = Province.objects.get(province_code = province_code)
        producer_list = Producer.objects.filter(province_id=province)
        return Response(status=status.HTTP_200_OK, data ={"data" :  ProducerSerializer(producer_list, many=True).data})