from rest_framework import serializers
from userApp.models import User_registraton

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_registraton
        fields = '__all__'