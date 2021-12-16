from rest_framework import serializers
# a serilizer converts a queryset into a dictionary
# it enables the transfer of data to anf from a server

class HelloSerilizer(serializers.Serializer):
    '''Serializes a name field for testing out APIView'''
    name = serializers.CharField(max_length=10)
