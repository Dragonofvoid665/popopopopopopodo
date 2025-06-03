from rest_framework import serializers
from shop.models import *

class ProductSreializer(serializers.ModelSerializer):
    class Meta :
        model = Product
        fields = '__all__'


