# author sqz
# date 2020/3/2 10:44
# file_name serializers
from .models import *
from rest_framework import serializers

class BranchSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=20,min_length=3,error_messages={
        "max_length": "最多20个字",
        "min_length": "最少3个字"
    })

    def create(self, validated_data):
        instance=Branch.objects.create(**validated_data)
        return instance
    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.save()
        return instance

class StaffSerializer(serializers.Serializer):
    id = serializers.ImageField()
    name=serializers.CharField(max_length=20,min_length=3,error_messages={
        "max_length": "最多20个字",
        "min_length": "最少3个字"
    })

    def validate(self, attrs):
        try:
            b = Branch.objects.get(name=attrs['breach']['name'])
            attrs['breach'] = b
        except:
            raise serializers.ValidationError('部门不存在')
        return attrs

    def create(self, validated_data):
        instance = Staff.objects.create(**validated_data)
        return instance
