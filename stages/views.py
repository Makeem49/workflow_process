from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Stage
from .serializers import StageSerializer, StageDetailSerializer
from process.models import Process

class StageCreateView(generics.CreateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field='pk'


    def create(self, request, *args, **kwargs):
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(process=process)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class StageListView(generics.ListAPIView):
    serializer_class = StageSerializer

    def get_queryset(self):
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        queryset = Stage.objects.filter(process=process)
        return queryset
    
    def get_serializer_context(self):
        process_name = self.kwargs['process_name']
        return {
            'request': self.request,
            'process_name': self.format_kwarg,
            'view': self,
            'process_name' : process_name
        }


class StageDetailView(generics.RetrieveAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageDetailSerializer
    lookup_url_kwarg = ['process_id']

    def get_object(self):
        stage_name = self.kwargs['stage_name']
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()

        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        stage = Stage.objects.filter(name=stage_name, process=process).first()

        return stage


class StageUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field='pk'

    def get_object(self):
        stage_id = self.kwargs['pk']
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        stage = Stage.objects.filter(id=stage_id, process=process).first()

        return stage


class StageDeactivateView(generics.DestroyAPIView):
    queryset = Stage.objects.all()
    serializer_class = StageSerializer
    lookup_field='pk'

    def get_object(self):
        stage_id = self.kwargs['pk']
        process_name = self.kwargs['process_name']
        process = Process.objects.filter(name__iexact=process_name).first()
        
        if not process:
            raise NotFound(detail='Process not found', code=status.HTTP_404_NOT_FOUND)
        
        stage = Stage.objects.filter(id=stage_id, process=process).first()

        return stage