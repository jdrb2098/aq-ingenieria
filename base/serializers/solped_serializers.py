from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Solped


class SolpedSerializer(serializers.ModelSerializer):
    class Meta:
        model= Solped
        fields = '__all__'