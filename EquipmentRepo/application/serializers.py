from rest_framework import serializers
from .models import Equipment,Executive

                
class EquipmentSerializers(serializers.ModelSerializer):   
    class Meta:
        model=Equipment
        fields="__all__"
        
class ExecutiveSerializers(serializers.ModelSerializer):
    class Meta:
        model=Executive
        fields="__all__"
        
        
        
    
