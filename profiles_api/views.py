from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Test API HelloApiView"""

    def get(self, request, format=None):
        """ returns the list of API fetaures """
        an_apiview = [
            'uses the methods as function (get, post, patch , put , delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic'
            'Is mapped manually to URL',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
