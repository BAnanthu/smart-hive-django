from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from api.models import Function, Category, Level
from api.serializers import FunctionSerializer, CategorySerializer, SubCategorySerializer, LevelSerializer


class FunctionView(generics.ListAPIView):
    queryset = Function.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = FunctionSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer


class SubCategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = SubCategorySerializer


class LevelView(generics.ListAPIView):
    queryset = Level.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = LevelSerializer