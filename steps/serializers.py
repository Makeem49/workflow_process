from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Step
from process.models import Process
from stages.models import Stage


class StepSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Step
        fields = ['url', 'name']


    def get_url(self, obj):
        request = self.context.get('request')
        url = reverse('step-detail', args=[obj.stage.process.name, obj.stage.name, obj.name], request=request)
        return url


# class StepQuerySerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Step
#         fields = [ 'name']


class StepDetailSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField(read_only=True)
    groups = serializers.SerializerMethodField(read_only=True)
    next_action = serializers.CharField(write_only=True)


    class Meta:
        model = Step
        fields = ['name', 'is_required','permissions', 'groups', 'next_action']


    def get_permissions(self, obj):
        perms = obj.permissions.all()
        permsissions = [{permission.id : permission.name} for permission in perms]
        return permsissions
    

    def get_groups(self, obj):
        groups = obj.groups.all()
        groups = [{group.id : group.name} for group in groups]
        return groups
    
