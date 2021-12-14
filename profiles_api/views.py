from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''Test API view'''

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