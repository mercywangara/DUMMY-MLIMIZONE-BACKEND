from django.contrib import admin
from .models import Crop
from .models import MarketPrice


admin.site.register(Crop)
admin.site.register(MarketPrice)

# Register your models here.
