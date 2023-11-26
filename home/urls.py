# 3RD PARTY IMPORTS
from django.urls import path
# LOCAL IMPORTS
from . import views


urlpatterns = [
    path('', views.index, name='home'),
]

