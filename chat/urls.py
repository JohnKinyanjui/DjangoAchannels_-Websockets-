from django.urls import path
from .views import *

urlpatterns = [
    path('', homepageView),
    path('room/', roomView, name='room' )
     
]
