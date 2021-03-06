from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializers

class HelloApiView(APIView):
    '''Test API view'''

    serializer_class = serializers.HelloSerilizer

    def get(self, request, format=None):
        '''Returns a list of APIView features'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview}) 
        # every http function must return a response object that is a dict or list.
        # it coverts the list or dict into a JSON file to then process

    def post(self, request):
        '''Create a hello message with our name'''
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST,
            )

    def put(self, request, pk=None):
        '''Handle updating object'''
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        '''
        Handle partial update of an object
        For example: it could be used to just update 
        as opposed to the whole object
        '''
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        '''Handle deleting an object'''
        return Response({'method': 'DELETE'})