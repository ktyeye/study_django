from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from study_django.identify.models import Person, User

class BasePersonSerializer(serializers.ModelSerializer):
	class Meta :
		model = Person
		fields = ('id', 'name', 'phone', 'addr')
  
  
class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'email')


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password' : {"write_only" : True}}
        
        
    def create(self, validated_data):
        user = User.objects.create_user(
			validated_data["username"], None, validated_data["password"]
		)
        return user