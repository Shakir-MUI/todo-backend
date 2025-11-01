from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h2>Welcome to the Todo App Backend!</h2>")

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
