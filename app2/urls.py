from django.urls import path
from app2.views import *

urlpatterns=[
    path('a2_first/',a2_first,name='a2_first'),
    path('a2_second/',a2_second,name='a2_second'),
]