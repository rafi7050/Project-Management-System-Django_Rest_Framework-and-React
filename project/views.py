from django.shortcuts import render
import json
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import  TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/task-list',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>', 

    }
    return Response(api_urls)

@api_view(['GET'])
def tasklist(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)