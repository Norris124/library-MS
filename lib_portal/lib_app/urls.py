from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('Admin', Admin),
    path('Student', Students),
    # path('save',save_student),
    path('students',Students_tab),
    path('students/add',save_student),
    path('Books',Books),
    path('Returns',Returns),
]
