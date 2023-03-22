from rest_framework import generics, status
from django.contrib.auth.models import Permission, Group
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

from .serializers import (
            GrantPermissionSerializer, 
            AssignStageSerializer, 
            GrantGroupSerializer
            )
from process.models import Process
from stages.models import Stage
from steps.models import Step



class GrantPermissionCreateListView(generics.ListCreateAPIView):
    """ This view helps to create and list existing permissions """
    serializer_class = GrantPermissionSerializer
    queryset = Permission.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GrantPermissionUpdateView(generics.RetrieveUpdateAPIView):
    """This view help to allow existing permission to be updated """
    serializer_class = GrantPermissionSerializer
    queryset = Permission.objects.all()
    lookup_field = 'pk'


class GrantPermissionDeleteView(generics.RetrieveDestroyAPIView):
    """This view help to allow existing permission to be deleted"""
    serializer_class = GrantPermissionSerializer
    queryset = Permission.objects.all()
    lookup_field = 'pk'


class AssignStagePermissionView(generics.RetrieveUpdateAPIView):
    """This view is use to dynamically add permission to a stage instance"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()
        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        stage.permissions.add(permission)
        stage.save()

        return super().perform_update(serializer)
    

class AssignProcessPermissionView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add permission to a stage instance"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        process.permissions.add(permission)
        process.save()

        return super().perform_update(serializer)


class AssignStepPermissionView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add permission to a stage instance"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        step_name = self.kwargs['step_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        
        step = Step.objects.filter(name=step_name, stage=stage).first()
        
        if not step:
            raise NotFound(detail='Step not found', code=status.HTTP_404_NOT_FOUND)
        step.permissions.add(permission)
        step.save()

        return super().perform_update(serializer)


class GrantGroupCreateListView(generics.ListCreateAPIView):
    """This view helps to create and list existing group.
    
    Inside this view, a group can be created and add existing permissions to it, or just create the group alone. 
    """
    serializer_class = GrantGroupSerializer
    queryset = Group.objects.all()


class GrantGroupUpdateView(generics.RetrieveUpdateAPIView):
    """This view help to allow existing group to be updated """
    serializer_class = GrantGroupSerializer
    queryset = Group.objects.all()


class GrantGroupDeleteView(generics.RetrieveDestroyAPIView):
    """This view help to allow existing group to be deleted"""
    serializer_class = GrantGroupSerializer
    queryset = Group.objects.all()


class AssignGroupPermissionView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add permission to gorup"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        group_name = self.kwargs['group_name']
        group = Group.objects.filter(name__iexact=group_name).first()
        if not group:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        group.permissions.add(permission)
        group.save()

        return super().perform_update(serializer)


class AssignGroupProcessView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add group to a particular instance of a process"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        process.groups.add(group)
        process.save()
        return super().perform_update(serializer)



class AssignGroupStageView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add group to a particular instance of a stage"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        stage_name = self.kwargs['stage_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        

        stage.groups.add(group)
        stage.save()
        return super().perform_update(serializer)


class AssignGroupStepView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add group to a particular instance of a step"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        stage_name = self.kwargs['stage_name']
        step_name = self.kwargs['step_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()
        step = Step.objects.filter(name__iexact=step_name, stage=stage).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        

        if not step:
            raise NotFound(detail='Step not found', code=status.HTTP_404_NOT_FOUND)        

        step.groups.add(group)
        step.save()
        return super().perform_update(serializer) 


class RemoveStagePermission(generics.RetrieveUpdateAPIView):
    """This view is use remove a permission on a given stage instance"""

    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']

        process = Process.objects.filter(name__iexact=process_name).first()
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()
        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        stage.permissions.remove(permission)
        stage.save()

        return super().perform_update(serializer)


class RemoveProcessPermissionView(generics.RetrieveUpdateAPIView):
    """This view is use to dynamically remove permission to a stage instance"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        process.permissions.remove(permission)
        process.save()

        return super().perform_update(serializer)
    

class RemoveStepPermissionView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically remove permission to a stage instance"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        step_name = self.kwargs['step_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        
        step = Step.objects.filter(name=step_name, stage=stage).first()
        
        if not step:
            raise NotFound(detail='Step not found', code=status.HTTP_404_NOT_FOUND)
        step.permissions.remove(permission)
        step.save()

        return super().perform_update(serializer)
    

class RemoveGroupPermissionView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically remove permission to gorup"""
    serializer_class = AssignStageSerializer
    queryset = Permission.objects.all()

    def perform_update(self, serializer):
        permission = self.get_object()

        group_name = self.kwargs['group_name']
        group = Group.objects.filter(name__iexact=group_name).first()
        if not group:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        group.permissions.remove(permission)
        group.save()

        return super().perform_update(serializer)
    

class RemoveGroupProcessView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically remove group to a particular instance of a process"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        process.groups.remove(group)
        process.save()
        return super().perform_update(serializer)
    

class AssignGroupStageView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add group to a particular instance of a stage"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        stage_name = self.kwargs['stage_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        

        stage.groups.remove(group)
        stage.save()
        return super().perform_update(serializer)
    


class RemoveGroupStepView(generics.RetrieveUpdateAPIView):
    """This view is used to dynamically add group to a particular instance of a step"""
    queryset = Group.objects.all()
    serializer_class = GrantGroupSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        group = self.get_object()
        process_name = self.kwargs['process_name']
        stage_name = self.kwargs['stage_name']
        step_name = self.kwargs['step_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()
        step = Step.objects.filter(name__iexact=step_name, stage=stage).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        if not stage:
            raise NotFound(detail='Stage not found', code=status.HTTP_404_NOT_FOUND)
        

        if not step:
            raise NotFound(detail='Step not found', code=status.HTTP_404_NOT_FOUND)        

        step.groups.remove(group)
        step.save()
        return super().perform_update(serializer) 