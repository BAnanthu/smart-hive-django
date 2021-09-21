from django.db import models


# Create your models here.

class Function(models.Model):
    function_name = models.CharField(max_length=30)

    def __str__(self):
        return self.function_name


class Category(models.Model):
    function_id = models.ForeignKey(Function,related_name='category', on_delete=models.CASCADE)
    category_name = models.CharField(max_length=30)
    category_tag = models.CharField(max_length=10)
    category_details = models.TextField()

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category_id = models.ForeignKey(Category,related_name='sub_category', on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=30)
    subcategory_details = models.TextField()

    def __str__(self):
        return self.subcategory_name


class Level(models.Model):
    level_name = models.CharField(max_length=40)
    score_type = models.CharField(max_length=30)

    def __str__(self):
        return self.level_name


class Option(models.Model):
    level_id = models.ForeignKey(Level, related_name='options',  on_delete=models.CASCADE)
    option = models.CharField(max_length=30)

    def __str__(self):
        return self.option


