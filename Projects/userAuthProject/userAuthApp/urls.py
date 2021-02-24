from django.urls import path
from .views import *

urlpatterns=[
    path("",userView,name='userView'),
    path('user/logout',userLogOut,name='userLogOut'),
    path('user/form/<int:id>',userForm,name='userForm'),
    path('user/repView/<int:repId>',userRepoView,name='userRepoView'),

#-----------------Admin urls---------------------
    path('adm',adminPanel,name='admin'),
    path("adm/createUser",createUser,name="createUser"),
    path('adm/editUser/<int:id>',editUser),
    path("adm/createClient",createClient,name="createClient"),
    path("adm/reports/<int:id>",reportView,name="report"),
    path("adm/reports/view/<int:id>",insideViewRepo),
    path('adm/delReport/<int:id>',delReport),

    path("adm/log",adminLogOut,name="adminLogOut"),
#------------------USER urls-------------------------------
    path("login",login,name='login'),
    path('validate',validate),
]
