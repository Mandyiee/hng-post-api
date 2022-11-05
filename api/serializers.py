from rest_framework import serializers


class Enumserializser(serializers.serializer):
    operation_type = serializers.Charfield(required=True, max_length=200)
    x = serializers.IntegerField(required=True)
    y = serializers.IntegerField(required=True)