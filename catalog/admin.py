from django.contrib import admin
from .models import Car, Color, Brand

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    
    list_display = ('brand', 'model_of_car', 'transmission', 'year',
                    'color')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandrAdmin(admin.ModelAdmin):
    pass


