# 3RD PARTY IMPORTS
from django.urls import path

# LOCAL IMPORTS
from . import views

urlpatterns = [
    path('blog/', views.PublishedPosts.as_view(), name='blog'),
    path('<slug:slug>/', views.PostExpand.as_view(), name='post_expand'),
]