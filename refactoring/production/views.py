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
        result = ProvinceSerializer.create(request.data)
        return Response(status=status.HTTP_201_CREATED, data ={"data" :  ProvinceSerializer(result).data})

class ProvinceDemandView(APIView):
    def patch(self, request,province_code):
        if ProvinceSerializer.validate_demand(request.data):
            result = ProvinceSerializer.update_demand(province_code,request.data)
            return Response(status=status.HTTP_200_OK, data ={"data" :  ProvinceSerializer(result).data})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

class ProvinceShortfallView(APIView):
    def get(self,request,province_code):
        result =ProvinceSerializer.get_shortfall(province_code)
        return Response(status=status.HTTP_200_OK, data ={"data" :  result})

class ProvinceProfitView(APIView):
    def get(self,request,province_code):
        result =ProvinceSerializer.get_profit(province_code)
        return Response(status=status.HTTP_200_OK, data ={"data" :  result})

class ProducerView(APIView):
    def post(self, request):
        result = ProducerSerializer.create(request.data)
        return Response(status=status.HTTP_201_CREATED, data ={"data" :  ProducerSerializer(result).data})


class ProducerListView(APIView):
    def get(self, request, province_code):
        province = Province.objects.get(province_code = province_code)
        result = Producer.objects.filter(province_id=province)
        return Response(status=status.HTTP_200_OK, data ={"data" :  ProducerSerializer(result, many=True).data})

class ProducerProductionView(APIView):
    def patch(self, request, producer_name):
        result = ProducerSerializer.update_production(producer_name, request.data)
        return Response(status=status.HTTP_200_OK, data = {"data" : ProducerSerializer(result).data})