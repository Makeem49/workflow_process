from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Step
from process.models import Process


class StepSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Step
        fields = ['url', 'name']


    def get_url(self, obj):
        request = self.context.get('request')
        url = reverse('step-detail', args=[obj.stage.process.name, obj.stage.name, obj.name], request=request)
        return url


class StepDetailSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Step
        fields = ['name', 'permissions', 'groups', 'next_action']


    def get_permissions(self, obj):
        perms = obj.permissions.all()
        permsissions = [{permission.id : permission.name} for permission in perms]
        return permsissions
    

    def get_groups(self, obj):
        groups = obj.groups.all()
        groups = [{group.id : group.name} for group in groups]
        return groups
    
    
    # def get_next_action(self, obj):
    #     # process = Process.objects.filter(stage=obj.stage).first()
    #     # steps = [stage for stage in process.stage_set.all()]
    #     # print(steps)
    #     return 'process'