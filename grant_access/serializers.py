from rest_framework import serializers
from django.contrib.auth.models import Permission, Group, ContentType
from django.contrib.auth import get_user_model
from django.forms.widgets import SelectMultiple
import json


class GrantPermissionSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)

    class Meta:
        model = Permission
        fields = ['id', 'name']

    def create(self, validated_data):
        User = get_user_model()
        content_type = ContentType.objects.get_for_model(User)
        name = validated_data.get('name')
        convert_to_list = name.split(' ')
        codename = '_'.join(convert_to_list)
        permission = Permission.objects.create(codename=codename, name=name, content_type=content_type)
        return permission
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    

class AssignStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Permission
        fields = ['name']


class GrantGroupSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    permissions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = ['id','name', 'permissions']

    def create(self, validated_data):
        # permissions_data = validated_data.pop('permissions')
        # if permissions_data:
        #     permissions_data = permissions_data.split(',')
        group = Group.objects.create(**validated_data)
        # for permission_name in permissions_data:
        #     permission = Permission.objects.get(name__iexact=permission_name)
        #     group.permissions.add(permission)
        return group

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    

    def get_permissions(self, obj):
        perms = obj.permissions.all()
        perm_serializer = GrantPermissionSerializer(perms, many=True).data
        return perm_serializer
    



    

    



    