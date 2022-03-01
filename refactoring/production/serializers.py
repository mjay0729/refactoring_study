from dataclasses import field
from webbrowser import get
from.models import Province, Producer
from rest_framework import serializers



class ProvinceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Province
        fields = '__all__'
    
    def create(self, validated_data):
        province = Province.objects.create(
            province_code = validated_data.get("code")
            , province_demand = validated_data.get("demand")
            , province_price = validated_data.get("price")
        )
        return province
    
    def get_shortfall(self, province_code):
        province = Province.objects.get(province_code=province_code)
        result = {
            "shortfall" : province.province_demand - province.province_total_production
        }
        return result

class ProducerSerializer(serializers.ModelSerializer):

    province_id = ProvinceSerializer()

    class Meta:
        model = Producer
        fields = '__all__'
    
    def create(self, validated_data):
        province = Province.objects.get(province_code = validated_data.get("province_code"))
        producer = Producer.objects.create(
            province_id = province
                , producer_name = validated_data.get("name")
                , producer_cost = validated_data.get("cost")
                , producer_production = validated_data.get("production")
                )
        ProducerSerializer.update_total_production(province, int(validated_data.get("production")))
        return producer

    def update_total_production(province,production):
        province.province_total_production += production
        province.save()
