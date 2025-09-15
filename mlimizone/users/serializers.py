from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'role', 'phone_number']

    def validate_role(self, value):
        # Only allow registration as wholesaler
        if value != 'wholesaler':
            raise serializers.ValidationError("Registration is only allowed for wholesalers.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user