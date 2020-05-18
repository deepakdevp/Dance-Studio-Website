from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import messageSerializer
from rest_framework.response import Response
from rest_framework import status,generics

def home(request):
    return render(request, 'index.html', {})

class message(APIView):
    serializer_class = messageSerializer
    def post(self, request):
        if request.method == 'POST':
            print(request.data)
            serializer = messageSerializer(data=request.data)
            if serializer.is_valid():
                print(serializer)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)