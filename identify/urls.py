from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.Login.as_view(),name='login'),
    path('logout/', views.logout, name="logout"),
    path('', login_required(views.Nist.as_view()),name='IDENTIFY (ID)'),
    path('identify/', views.Identify.as_view(),name='IDENTIFY (ID)'),
    path('protect/', views.Protect.as_view(),name='PROTECT (PR)'),
    path('detect/', views.Detect.as_view(),name='DETECT (DE)'),
    path('respond/', views.Respond.as_view(),name='RESPOND (RS)'),
    path('recover/', views.Protect.as_view(),name='RECOVER (RC)'),
    # path('recover/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Protect.as_view(),name='RECOVER (RC)'),
]



