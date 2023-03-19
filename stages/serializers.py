from rest_framework import serializers
from .models import Stage
from rest_framework.reverse import reverse
from steps.serializers import StepSerializer


class StageSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField(read_only=True)
    initial_stage = serializers.SerializerMethodField(read_only=True)
    final_stage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Stage
        fields = ['url', 'name', 'initial_stage', 'final_stage']

    def get_url(self, obj):
        request = self.context.get('request')
        url = reverse('stage-detail', args=[obj.process.id, obj.id], request=request)
        return url
    
    def get_initial_stage(self, obj):
        return obj.is_initial_stage

    def get_final_stage(self, obj):
        return obj.is_final_stage


    
class StageDetailSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Stage
        fields = ['actions']


    def get_actions(self, obj):
        steps = obj.step_set.all()
        request = self.context.get('request')
        steps_data = StepSerializer(steps, many=True, context={'request': request}).data
        return steps_data
    