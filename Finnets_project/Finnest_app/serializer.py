from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class Person_Details(serializers.ModelSerializer):
    class Meta:
        model  = Personn
        fields = '__all__'

class CustomLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid username or password.")

        if not user.is_active:
            raise serializers.ValidationError("User is not active.")

        data['user'] = user
        return data 
    
# class ModuleListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ModuleList
#         fields = '__all__'      
    
class ModuleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleList
        fields = ['id','name']       

class ModulePermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModulePermission
        fields = [ 'id','moduleid','userid','canAccess','canCreate','canEdit','canDelete']
        
        
        