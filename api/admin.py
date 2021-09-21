from django.contrib import admin

# Register your models here.
from api.models import Function, Category, SubCategory, Level, Option

admin.site.register(Function)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Level)
admin.site.register(Option)