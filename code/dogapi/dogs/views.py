from django.shortcuts import render
from django.http import HttpResponse
from dogs.models import Dog
from rest_framework import viewsets
from rest_framework import serializers


# Create your views here.
def index(request):
    return HttpResponse("Hello My people")

class DogSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=40)
    breed = serializers.CharField(max_length=40)

class DogViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing dog instances.
    """
    serializer_class = DogSerializer
    queryset = Dog.objects.all()