from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #Accepts the following inputs only for an argument inputed
        fields = ['id','username','password']
        #Input password should not be returned after the user have inserted the password
        extra_kwargs = {'password':{'write_only':True}}
    #Creates a new user
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data)
        return user
    
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','title','content','created_at','author']
        extra_kwargs = {'author':{'read_only':True}}