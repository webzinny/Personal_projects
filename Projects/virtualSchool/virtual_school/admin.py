from django.contrib import admin
from .models import *

class student_listAdmin (admin.ModelAdmin):
    list_display = ['id','school_id','roll_no','name','Class','email','phone','password']

class teacher_listAdmin (admin.ModelAdmin):
    list_display = ['id','school_id','name','email','phone','password']

class school_listAdmin (admin.ModelAdmin):
    list_display = ['id','school_name','name','email','phone','password']

class homeworkAdmin (admin.ModelAdmin):
    list_display=['school_id','student_id','student_name','name','Class','subject','date','file']

class chatAdmin (admin.ModelAdmin):
    list_display=['id','school_id','Class','person_id','name','date','message']

class teacher_hwAdmin(admin.ModelAdmin):
    list_display=['id','school_id','Class','subject','date','name','file']

class notesAdmin(admin.ModelAdmin):
    list_display=['id','school_id','teacher_id','Class','subject','date','name','file']

class noticeAdmin(admin.ModelAdmin):
    list_display=['id','school_id','teacher_id','date','notice_msg']

class lecturesAdmin(admin.ModelAdmin):
    list_display=['id','school_id','teacher_id','Class','subject','link']

class infoAdmin(admin.ModelAdmin):
    list_display=['id','school_id','teacher_id','Class','type','file']


admin.site.register(student_list,student_listAdmin)
admin.site.register(teacher_list,teacher_listAdmin)
admin.site.register(school_list,school_listAdmin)
admin.site.register(homework,homeworkAdmin)
admin.site.register(chat,chatAdmin)
admin.site.register(teacher_hw,teacher_hwAdmin)
admin.site.register(notes,notesAdmin)
admin.site.register(notice,noticeAdmin)
admin.site.register(lectures,lecturesAdmin)
admin.site.register(info,infoAdmin)
