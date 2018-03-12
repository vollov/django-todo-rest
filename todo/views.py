#from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from todo.models import Todo
from todo.serializers import TodoSerializer

#from django.conf import settings

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created')
    serializer_class = TodoSerializer
