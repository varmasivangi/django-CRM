from django.urls import path
from . import views

urlpatterns = [
    path('',views.teachers_list,name="all-teacher"),
    path('add-teacher/',views.add_teachers,name="addteacher")
]