from django.urls import path
from . import views


urlpatterns = [
    path('identify/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Identify.as_view(),name='IDENTIFY (ID)'),
    path('protect/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Protect.as_view(),name='PROTECT (PR)'),
    path('detect/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Detect.as_view(),name='DETECT (DE)'),
    path('respond/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Respond.as_view(),name='RESPOND (RS)'),
    path('recover/<int:category_id>/<int:subcategory_id>/<int:level_id>', views.Protect.as_view(),name='RECOVER (RC)'),
]



