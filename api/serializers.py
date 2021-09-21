from rest_framework import serializers

from api.models import Function, Category, SubCategory, Level, Option


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_category = SubCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id','category_name','category_tag','category_details','function_id','sub_category']


class FunctionSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = Function
        fields = ['id', 'function_name','category']


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = "__all__"


class LevelSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True)

    class Meta:
        model = Level
        fields = ['id','level_name','score_type','options']
