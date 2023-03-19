from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User serializer"""
    password = serializers.CharField(write_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
        lookup_field='pk',
        read_only=True
    )

    class Meta:
        model = User
        fields = ['url','email', 'first_name', 'last_name',
            'password', 'is_active']

    def create(self, validated_data):
        instance = User.objects.create(**validated_data)
        return instance