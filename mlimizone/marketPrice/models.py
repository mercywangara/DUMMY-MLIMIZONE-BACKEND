from django.db import models

# Create your models here.


class Crop(models.Model):
    crop_id = models.AutoField(primary_key= True)
    crop_name = models.CharField(max_length= 50)
    crop_code = models.CharField(max_length= 50)

    def __str__ (self):
        return self.crop_name


class MarketPrice(models.Model):
    market_price_id = models.AutoField(primary_key= True)
    crop_id = models.ForeignKey(Crop, on_delete=models.CASCADE)
    location = models.CharField(max_length= 20)
    price_per_unit = models.DecimalField(decimal_places= 2, max_digits=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Market Price for {self.market_price_id} is {self.price_per_unit}"