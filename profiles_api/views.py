from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview=[
            'uses HTTP methods as fct (get,post,patch,put,delete)',
            'is similar to a traditional django view',
            'Gives you the most control over your app logic',
            'is mapped manually to url',
        ]

        return Response({'message':'Hello', 'an_apiview':an_apiview})


    def post(self, request):
        """creat a hello msg with our name"""
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'hello Mr {name}'
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response ({'method':'PUT'})
    def patch(self, request, pk:None):
        """partial update"""
        return Response({'method':'PATCH'})
    def delete(self, request, pk=None):
        return Response({'method':'DELETE'})
