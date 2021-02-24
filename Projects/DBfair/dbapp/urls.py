from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('',home),
    path('admins',adminLogin),
    path('adminDashboard',adminDashboard),
    path('adminLogOut',adminLogOut,name='adminLogOut'),
    path('adminContent',adminContent,name='adminContent')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
