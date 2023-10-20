from unicodedata import name
from django.urls import path
from . import views
app_name='classapp'

urlpatterns=[
    path('home/',views.TaskListView.as_view(),name="home"),

    path('show/<int:pk>/',views.TaskDetailtView.as_view(),name="show"),

    path('update/<int:pk>/',views.TaskUpdateView.as_view(),name="update"),

    path('delete/<int:pk>/',views.TaskDeletetView.as_view(),name="delete")

    ]