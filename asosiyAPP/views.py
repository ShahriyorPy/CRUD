# from django.shortcuts import render
from rest_framework.views import APIView
# from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class ContactsAPIView(APIView):
    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)

class ContactAPIView(APIView):
    def get(self, request, pk):
        contact = Contact.objects.get(id=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def delete(self, instance, pk):
        contact = Contact.objects.filter(id=pk).delete()
        data = {
            "success": True,
            "xabar": "Contact o'chirildi!"
        }
        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        contact = Contact.objects.get(id=pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_406_NOT_ACCEPTABLE)
