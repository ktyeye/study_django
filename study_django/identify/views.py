from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person
from .serializers import BasePersonSerializer, EmailSerializer


# Create your views here.
@api_view(['GET'])
def PersonAPI (request, id):
    now_person = Person.object.get(id=id);