from rest_framework import serializers
from .models import *
class userserializer(serializers.ModelSerializer):
    class Meta:
        model = modelusers
        fields = '__all__'
class timedoctorserializer(serializers.ModelSerializer):
    class Meta:
        model = modeltimedoctor
        fields = '__all__'
class messagesserializer(serializers.ModelSerializer):
    class Meta:
        model = modelmessages
        fields = '__all__'
