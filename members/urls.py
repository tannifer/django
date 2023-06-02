from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('json/', views.json,name='jason'),
    path('members/details/<int:id>',views.details,name='details'),
    path('members/details/<int:id>',views.details,name='details'),
]
