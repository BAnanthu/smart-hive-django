from . import views
from django.urls import path

urlpatterns = [
    path('function/', views.FunctionView.as_view()),
    path('options/', views.LevelView.as_view()),
    # path('fun/<int:id>',views.getObject),
    path('functions/',views.GetFunctions.as_view()),
    path('Category/',views.GetCategory.as_view()),
    path('sub-category/',views.GetSubCategory.as_view()),
    path('level/',views.GetLevel.as_view()),
    path('options/',views.GetOptions.as_view()),
]
