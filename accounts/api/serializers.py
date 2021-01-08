from rest_framework import serializers
from accounts.models import CustomAccount

class CustomAccountDisplaySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CustomAccount
        fields = ['username']