from django.urls import path
from .views import home
from .views import greet
from .views import class_area

urlpatterns = [
    path('', home, name='home'),
    path('greet/',greet,{'name': 'Guest'},name="greet_default"),
    path('greet/<str:name>/', greet, name='greet'),
        path('area/', class_area, name='class_area'),


]
