from rest_framework import serializers
from .models import Process
from stages.serializers import StageSerializer


class ProcessSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='process-detail',
        lookup_field = 'pk',
        read_only=True
    )

    class Meta:
        model = Process
        # fields = ['url', 'name']
        fields = ['url', 'name']

    
class ProcessDetailSerializer(serializers.ModelSerializer):
    stages = serializers.SerializerMethodField(read_only=True)
    permissions = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Process
        fields = ['stages', 'permissions', 'groups']

    def get_stages(self, obj):
        stages = obj.stage_set.all()
        request = self.context.get('request')
        stages = StageSerializer(stages, many=True, context={'request': request}).data
        return stages
    
    def get_permissions(self, obj):
        perms = obj.permissions.all()
        permsissions = [{permission.id : permission.name} for permission in perms]
        return permsissions
    
    def get_groups(self, obj):
        groups = obj.groups.all()
        groups = [{group.id : group.name} for group in groups]
        return groups
