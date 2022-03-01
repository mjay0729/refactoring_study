from django.db import models



class Province(models.Model):
    province_id = models.AutoField(primary_key=True)
    province_code = models.CharField(unique=True, max_length=20)
    province_total_production = models.IntegerField(default = 0)
    province_demand = models.IntegerField()
    province_price = models.IntegerField()


class Producer(models.Model):
    producer_id = models.AutoField(primary_key=True)
    province_id = models.ForeignKey("Province", on_delete=models.CASCADE, db_column="province_id")
    producer_name = models.CharField(unique=True, max_length=20)
    producer_cost = models.IntegerField()
    producer_production = models.IntegerField()