from django.contrib import admin
from .models import BJPdata

class BJPdataAdmin(admin.ModelAdmin):
    list_display=['id','Date','Designation','Name','Place','Contact','Sess']

admin.site.register(BJPdata,BJPdataAdmin)
