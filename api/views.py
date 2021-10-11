from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
# Create your views here.
from api.models import Function, Category, Level, SubCategory2, Option
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


import json
from django.core import serializers


class GetFunctions(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        function_name = [{'id': function.id, 'name': function.function_name} for function in Function.objects.all()]
        return Response(function_name)


class GetCategory(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        category_name = [{'id': category.id, 'name': category.category_name, 'function_id': category.function_id.id} for
                         category in Category.objects.all()]
        return Response(category_name)


class GetSubCategory(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        subcategory = [
            {'id': subcategory.id, 'name': subcategory.subcategory_name, 'detail': subcategory.subcategory_details,
             'category_id_id': subcategory.category_id.id} for subcategory in SubCategory2.objects.all()]
        return Response(subcategory)


class GetLevel(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        subcategory = [{'id': level.id, 'name': level.level_name, 'score_type': level.score_type} for level in
                       Level.objects.all()]
        return Response(subcategory)


class GetOptions(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        subcategory = [{'id': option.id, 'name': option.option} for option in
                       Option.objects.all()]
        return Response(subcategory)



# def getFunctions(request):
#     SomeModel_json = serializers.serialize("json", Function.objects.all())
#     data = {"data": SomeModel_json}
#     return JsonResponse(data, content_type="text/json-comment-filtered")

# def getObject(request, id):
#     obj = Function.objects.get(pk=id)
#     data = serializers.serialize('json', [obj,])
#     struct = json.loads(data)
#     data = json.dumps(struct[0])
#     return HttpResponse(data, content_type='application/json')
