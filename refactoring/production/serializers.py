from dataclasses import field
from webbrowser import get
from.models import Province, Producer
from rest_framework import serializers



class ProvinceSerializer(serializers.ModelSerializer):
    
    province_demand = serializers.IntegerField()

    class Meta:
        model = Province
        fields = '__all__'
    
    def create(validated_data):
        province = Province.objects.create(
            province_code = validated_data.get("code")
            , province_demand = validated_data.get("demand")
            , province_price = validated_data.get("price")
        )
        return province
    
    def get_shortfall( province_code):
        province = Province.objects.get(province_code=province_code)
        result = {
            "shortfall" : province.province_demand - province.province_total_production
        }
        return result

    def get_profit( province_code):
        province = Province.objects.get(province_code=province_code)
        satisfied_demand = province.province_demand if province.province_demand < province.province_total_production else province.province_total_production
        demand_value = satisfied_demand *  province.province_price
        remaining_demand = province.province_demand
        demand_cost = ProvinceSerializer.get_demand_cost(province, remaining_demand)
        result = {
            "profit" : demand_value - demand_cost
        }
        return result
    
    def get_demand_cost(province,remaining_demand):
        result = 0
        producers = Producer.objects.filter(province_id = province).order_by('producer_cost')
        for producer in producers:
            contribution = remaining_demand if remaining_demand < producer.producer_production else producer.producer_production
            result += contribution * producer.producer_cost
        return result
        
    def update_demand( province_code,validated_data):
        province = Province.objects.get(province_code=province_code)
        province.province_demand = validated_data.get("demand")
        province.save()

    def validate_demand(data):
        try:
            int(data.get("demand"))
            return True
        except Exception:
            return False

class ProducerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producer
        fields = '__all__'
    
    
    def create(validated_data):
        province = Province.objects.get(province_code = validated_data.get("province_code"))
        producer = Producer.objects.create(
            province_id = province
                , producer_name = validated_data.get("name")
                , producer_cost = validated_data.get("cost")
                , producer_production = validated_data.get("production")
                )
        ProducerSerializer.update_total_production(province,producer)
        return producer

    def update_total_production(province,producer, new_production=None):
        province.province_total_production += int(producer.producer_production) if new_production is None else new_production - int(producer.producer_production)
        province.save()

    def update_production( producer_name, validated_data):
        producer = Producer.objects.get(producer_name=producer_name)
        province = producer.province_id
        ProducerSerializer.update_total_production(province,producer,int(validated_data.get("production")))
        producer.producer_production = validated_data.get("production")
        producer.save()
        return producer

