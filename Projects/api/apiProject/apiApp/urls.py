from django.urls import path
from .views import  *


urlpatterns=[
    path("test",test),
    path("validate",validate),
    path("data",getData),
    path('user/<int:id>',studentData),
]
