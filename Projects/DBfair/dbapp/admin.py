from django.contrib import admin
from dbapp.models import *

class categoryContentAdmin(admin.ModelAdmin):
    list_display=['id','tag','description','img']

admin.site.register(categoryContent,categoryContentAdmin)
