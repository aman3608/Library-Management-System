from unicodedata import name
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from library.serializers import RegisterSerializer
from .models import Book
from django.shortcuts import render

# Create your views here.
def homePage(request):
    return(request,"index.html")
class BookController(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self,request,id):
        return Response(Book.objects.filter(id=id).values())

    def put(self,request,id):
        data = request.data
        try:
            book=Book.objects.filter(id=data.get("id")).update(**data)
        except Exception:
            return Response({"message":"Internal server error"},status=500)

        return Response({"message": "Books inserted sucessfully","payload":data})

    def delete(self,request,id):
        try:
            book=Book.objects.filter(id=id).delete()
        except Exception:
            return Response({"message":"Internal server error"},status=500)

        return Response({"message": "Books deleted sucessfully","payload":id})


class BooksController(APIView):
    def get(self,request):
        return Response(Book.objects.all().values())
    
    def post(self, request):
        body = request.data
        try :
            newbook = Book.objects.create(**body)
        except Exception:
            return Response({"message": "Internal server error"},status=500)

        return Response({"message": "Books inserted sucessfully"},status=201)

from django.contrib.auth import get_user_model
class Registration(APIView):
    def post(self,request):
        serializer=RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":  "User created sucessfully"},status=201)
        return Response({"message":  "User not created"},status=500)






