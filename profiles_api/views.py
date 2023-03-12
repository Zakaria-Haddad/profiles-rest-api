from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'uses HTTP methods as fct (get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your app logic',
            'is mapped manually to url',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})
