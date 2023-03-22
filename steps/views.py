from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from .models import Step
from stages.models import Stage
from process.models import Process
from .serializers import StepSerializer, StepDetailSerializer
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

class StepCreateView(generics.CreateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    lookup_field='pk'

    def create(self, request, *args, **kwargs):
        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']

        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        

        if not stage:
            raise NotFound(detail='Stage not found.', code=status.HTTP_404_NOT_FOUND)
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(stage=stage)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class StepListView(generics.ListAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer 
    lookup_field='pk'

    def get_queryset(self):
        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']

        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        if not stage:
            raise NotFound(detail='Stage not found.', code=status.HTTP_404_NOT_FOUND)
        
        queryset = Step.objects.filter(stage=stage)

        return queryset


class StepDetailView(generics.RetrieveUpdateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepDetailSerializer 
    lookup_field='pk'

    def get_object(self):

        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        step_name = self.kwargs['step_name']

        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        if not stage:
            raise NotFound(detail='Stage not found.', code=status.HTTP_404_NOT_FOUND)
        
        obj = Step.objects.filter(name__iexact= step_name, stage=stage).first()

        if not obj:
            raise NotFound(detail='Step not found.', code=status.HTTP_404_NOT_FOUND)

        return obj


class StepUpdateView(generics.UpdateAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    lookup_field='pk'

    def get_object(self):
        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        step_name = self.kwargs['step_name']

        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        if not stage:
            raise NotFound(detail='Stage not found.', code=status.HTTP_404_NOT_FOUND)
        
        obj = Step.objects.filter(name__iexact= step_name, stage=stage).first()

        if not obj:
            raise NotFound(detail='Step not found.', code=status.HTTP_404_NOT_FOUND)

        return obj


class StepDeactivateView(generics.DestroyAPIView):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    lookup_field='pk'

    def get_object(self):
        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        step_name = self.kwargs['step_name']
        

        process = Process.objects.filter(name__iexact=process_name).first()
        stage = Stage.objects.filter(name__iexact=stage_name, process=process).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        if not stage:
            raise NotFound(detail='Stage not found.', code=status.HTTP_404_NOT_FOUND)
        
        obj = Step.objects.filter(name__iexact= step_name, stage=stage).first()

        if not obj:
            raise NotFound(detail='Step not found.', code=status.HTTP_404_NOT_FOUND)

        return obj