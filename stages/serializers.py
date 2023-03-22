from rest_framework import serializers
from .models import Stage
from rest_framework.reverse import reverse
from steps.serializers import StepSerializer


class StageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Stage
        fields = ['url', 'name', 'is_initial_stage', 'is_final_stage']

    def get_url(self, obj):
        request = self.context.get('request')
        print(obj.name)
        url = reverse('stage-detail', args=[obj.process.name, obj.name], request=request)
        return url



    
class StageDetailSerializer(serializers.ModelSerializer):
    steps = serializers.SerializerMethodField(read_only=True)
    permissions = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Stage
        fields = ['steps', 'permissions', 'groups']


    def get_steps(self, obj):
        steps = obj.step_set.all()
        request = self.context.get('request')
        steps_data = StepSerializer(steps, many=True, context={'request': request}).data
        return steps_data
    
    def get_permissions(self, obj):
        perms = obj.permissions.all()
        permsissions = [{permission.id : permission.name} for permission in perms]
        return permsissions
    

    def get_groups(self, obj):
        groups = obj.groups.all()
        groups = [{group.id : group.name} for group in groups]
        return groups
    