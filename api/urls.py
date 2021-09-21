from . import views
from django.urls import path

urlpatterns = [
    path('function/', views.FunctionView.as_view()),
    path('options/', views.LevelView.as_view())
]
