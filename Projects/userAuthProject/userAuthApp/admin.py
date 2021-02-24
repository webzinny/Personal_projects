from django.contrib import admin
from .models import *

class userAdmin(admin.ModelAdmin):
    list_display=['id','name','email','pas','status','rep']

class clientAdmin(admin.ModelAdmin):
    list_display=['id','name']

class reportAdmin(admin.ModelAdmin):
    list_display=['id','client','name','date']

admin.site.register(user,userAdmin)
admin.site.register(client,clientAdmin)
admin.site.register(report,reportAdmin)
