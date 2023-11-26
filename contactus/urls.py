# 3RD PARTY IMPORTS
from django.urls import path
# LOCAL IMPORTS
from contactus import views

urlpatterns = [
    path('contactus/', views.ContactMessage.as_view(), name='contactus'),
]