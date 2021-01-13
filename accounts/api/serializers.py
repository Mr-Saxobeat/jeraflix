from rest_framework import serializers
from accounts.models import CustomAccount, Profile

class ProfileSerializer(serializers.ModelSerializer):
    main_profile = serializers.BooleanField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class CustomAccountDisplaySerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomAccount
        fields = ['id', 'username', 'profiles']