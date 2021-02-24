from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from datetime import date

def home (request):
    if request.method=="POST":
        if request.POST.get('student_login_form') == 'on':
            email = request.POST['user_email']
            password = request.POST['password']
            try:
                data = student_list.objects.get(email=email)
                if data.password==password:
                    request.session['student_email'] = email
                    request.session['school_id'] = data.school_id
                    request.session['Class'] = data.Class
                    return redirect ('student')
                return render (request,'home.html',{'msg':'*Wrong Password'})
            except:
                return render (request,'home.html',{'msg':'*Email not found'})
        if request.POST.get('teacher_login_form') == 'on':
            email = request.POST['teacher_email']
            password = request.POST['password']
            try:
                data = teacher_list.objects.get(email=email)
                if data.password==password:
                    request.session['teacher_email'] = email
                    request.session['tech_school_id'] = data.school_id
                    request.session['teacher_id'] = data.id
                    return redirect ('teacher')
                return render (request,'home.html',{'msg':'*Wrong Password'})
            except:
                return render (request,'home.html',{'msg':'*Email not found'})
        if request.POST.get('school_reg_form') == 'on':
            return school_registration (request)
        if request.POST.get('teacher_reg_form') == 'on':
            return teacher_registration (request)
        if request.POST.get('student_reg_form') == 'on':
            return student_registration(request)
    try:
        if request.session['student_email']:
            return redirect ('student')
        if request.session['teacher_email']:
            return redirect ('teacher')
    except :
        return render(request,'home.html')


#regisration pages----------------------------------------------------------------------------------
def student_registration(request):
    school_id = request.POST['school_id']
    roll_no = request.POST['roll_no']
    name      = request.POST['name']
    email   = request.POST['email']
    phone  = request.POST['phone']
    password = request.POST['password']
    re_password = request.POST['re_password']
    Class   = request.POST['Class']
    if password==re_password:
        data = student_list(school_id=school_id,roll_no=roll_no,name=name,Class=Class,email=email,phone=phone,password=password)
        data.save()
        request.session['student_email'] = email
        request.session['school_id'] = school_id
        request.session['Class'] = Class
        return redirect ('student')
    return HttpResponse("Password doesn't match")

def teacher_registration (request):
    school_id = request.POST['school_id']
    name      = request.POST['name']
    email   = request.POST['email']
    phone  = request.POST['phone']
    password = request.POST['password']
    re_password = request.POST['re_password']
    if password==re_password:
        data = teacher_list(school_id=school_id,name=name,email=email,phone=phone,password=password)
        data.save()
        request.session['teacher_email'] = email
        request.session['tech_school_id'] = school_id
        return redirect ('teacher')
    return HttpResponse("Password doesn't match")

def school_registration (request):
    school_name = request.POST['school_name']
    name = request.POST['name']
    email = request.POST['email']
    contact = request.POST['contact']
    password = request.POST['password']
    re_password = request.POST['re-password']
    if password == re_password:
        data = school_list (school_name=school_name,name=name,email=email,phone=contact,password=password)
        data.save()
        temp_data = school_list.objects.get(email=email)
        return HttpResponse("<center> <h1>This site is under development <br> YOur school id is "+str(temp_data.id)+"</h1></center>")
    return render (request,'student registration.html')

#discussionpanel------------------------------------------------------------------------------------
def discussionpanel (request):
    try:
        if request.session['student_email'] :
            chat_data = chat.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'])
            student_data = student_list.objects.get(email=request.session['student_email'])
            student_id = str(student_data.id)
            if request.method=="POST":
                message = request.POST['message']
                data = chat(school_id=request.session['school_id'],Class=request.session['Class'],person_id=student_id,name=student_data.name,date=date.today(),message=message)
                data.save()
                return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
            return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
        if  request.session['teacher_email']:
            chat_data = chat.objects.filter(school_id=request.session['tech_school_id'])
            student_data = teacher_list.objects.get(email=request.session['teacher_email'])
            student_id = str(student_data.id)
            if request.method=="POST":
                message = request.POST['message']
                data = chat(school_id=request.session['tech_school_id'],person_id=student_id,name=student_data.name,date=date.today(),message=message)
                data.save()
                return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
            return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
    except :
        return redirect ('home')

def tech_discussionpanel (request):
    try:
        if  request.session['teacher_email']:
            chat_data = chat.objects.filter(school_id=request.session['tech_school_id'])
            student_data = teacher_list.objects.get(email=request.session['teacher_email'])
            student_id = str(student_data.id)
            if request.method=="POST":
                message = request.POST['message']
                data = chat(school_id=request.session['tech_school_id'],person_id=student_id,name=student_data.name,date=date.today(),message=message)
                data.save()
                return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
            return render (request,'discussionpanel.html',{'key':chat_data,'st_id':student_id})
    except :
        return redirect ('home')

#student---------------------------------------------------------------------------------------------
def student(request):
    try:
        if request.session['student_email']:
            data  = notice.objects.filter(school_id=request.session['school_id'])
            if request.GET.get('log')=='logout':
                del request.session['student_email']
                del request.session['school_id']
                del request.session['Class']
                return redirect ('home')
            return render (request,'studentui.html',{'key':data})
    except :
        return redirect ('home')

#----------------student homeWork---------------------------------------------------------------------
def student_homework (request):
    try:
        if request.session['student_email']:
            return render (request,'student homework.html')
    except :
        return redirect ('home')

def student_addhomework (request):
    try:
        if request.session['student_email']:
            if request.method == "POST"  :
                student_data = student_list.objects.get(email = request.session['student_email'])
                student_id = student_data.id
                subject = request.POST['subject']
                file = request.FILES['file']
                data = homework(school_id=request.session['school_id'], student_id=student_id,student_name=student_data.name, name=file.name,Class=request.session['Class'],subject=subject,date=date.today(),file=file)
                data.save()
                return redirect ('student/homework')
            return render (request,'addhomework.html')
    except :
        return redirect ('home')

def student_homework_english (request):
    try:
        if request.session['student_email']:
            data  = teacher_hw.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='English')
            return render (request,'st_tech_posted_hw.html',{'key':data,'key1':'English'})
    except :
        return redirect ('home')

def student_homework_hindi (request):
    try:
        if request.session['student_email']:
            data  = teacher_hw.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Hindi')
            return render (request,'st_tech_posted_hw.html',{'key':data,'key1':'Hindi'})
    except :
        return redirect ('home')

def student_homework_math (request):
    try:
        if request.session['student_email']:
            data  = teacher_hw.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Math')
            return render (request,'st_tech_posted_hw.html',{'key':data,'key1':'Math'})
    except :
        return redirect ('home')

def student_homework_science (request):
    try:
        if request.session['student_email']:
            data  = teacher_hw.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Science')
            return render (request,'st_tech_posted_hw.html',{'key':data,'key1':'Science'})
    except :
        return redirect ('home')

def student_homework_social_science (request):
    try:
        if request.session['student_email']:
            data  = teacher_hw.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Social science')
            return render (request,'st_tech_posted_hw.html',{'key':data,'key1':'Social Science'})
    except :
        return redirect ('home')

#---------------student notes-------------------------------------------------------------------------
def student_notes (request):
    try:
        if request.session['student_email']:
            return render (request,'student notes.html')
    except :
        return redirect ('home')

def student_notes_english (request):
    try:
        if request.session['student_email']:
            data = notes.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='English')
            return render (request,'posted_notes.html',{'key':data,'sub':"English"})
    except :
        return redirect ('home')

def student_notes_hindi (request):
    try:
        if request.session['student_email']:
            data = notes.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Hindi')
            return render (request,'posted_notes.html',{'key':data,'sub':"Hindi"})
    except :
        return redirect ('home')

def student_notes_math (request):
    try:
        if request.session['student_email']:
            data = notes.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Math')
            return render (request,'posted_notes.html',{'key':data,'sub':"Maths"})
    except :
        return redirect ('home')

def student_notes_science (request):
    try:
        if request.session['student_email']:
            data = notes.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Science')
            return render (request,'posted_notes.html',{'key':data,'sub':'Science'})
    except :
        return redirect ('home')

def student_notes_social_science (request):
    try:
        if request.session['student_email']:
            data = notes.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Social science')
            return render (request,'posted_notes.html',{'key':data,'sub':'Social Science'})
    except :
        return redirect ('home')

#-----------------------------------------------------------------------------------------------------
def student_notebook (request):
    try:
        if request.session['student_email']:
            return render (request,'student notebook.html')
    except :
        return redirect ('home')

#-------------------student lectures------------------------------------------------------------------

def student_lectures (request):
    try:
        if request.session['student_email']:
            data_eng = lectures.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='English')
            data_hindi = lectures.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Hindi')
            data_math = lectures.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Math')
            data_science = lectures.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Science')
            data_social = lectures.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],subject='Social science')
            return render (request,'student lectures.html',{'key':data_eng,'key1':data_hindi,'key2':data_math,'key3':data_science,'key4':data_social})
    except :
        return redirect ('home')

#--------------- student event -----------------------------------------------------------------------

def student_event (request):
    try:
        if request.session['student_email']:
            data_syllabus = info.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],type='Syllabus')
            data_time_table = info.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],type='Time table')
            data_event    = info.objects.filter(school_id=request.session['school_id'],Class=request.session['Class'],type='Event')
            return render (request,'student event.html',{'key':data_syllabus,'key1':data_time_table,'key2':data_event})
    except :
        return redirect ('home')

#-------------------teacher-----------------------------------------------------------------------------------------------

def teacher (request):
    try:
        if request.session['teacher_email']:
            data  = notice.objects.filter(school_id=request.session['tech_school_id'])
            if request.GET.get('log')=='logout':
                del request.session['teacher_email']
                del request.session['tech_school_id']
                del request.session['teacher_id']
                return redirect ('home')
            return render (request,'teacherui.html',{'key':data})
    except :
        return redirect ('home')

def teacher_homework (request):
    try:
        if request.session['teacher_email']:
            if request.method == "GET":
                Class = request.GET.get('Class')
                subject = request.GET.get('subject')
                data = homework.objects.filter(school_id=request.session['tech_school_id'],Class=Class,subject=subject)
                return render (request,'see hw.html',{'key':data})
            return render (request,'see hw.html')
    except :
            return redirect ('home')

def teacher_post_hw(request):
    try:
        if request.session['teacher_email']:
            if request.method == "POST":
                school_id = request.session['tech_school_id']
                Class = request.POST['Class']
                subject = request.POST['subject']
                file = request.FILES['file']
                data = teacher_hw(school_id=school_id,Class=Class,subject=subject,date=date.today(),name=file.name,file=file)
                data.save()
                return redirect ('teacher/homework')
            return render (request,'teacher homework.html')
    except :
            return redirect ('home')


def teacher_posted_hw(request):
    try:
        if request.session['teacher_email']:
                data =  teacher_hw.objects.filter(school_id=request.session['tech_school_id'])
                return render (request,'see posted work.html',{'key':data})
    except :
            return redirect ('home')


def teacher_notes (request):
    try:
        if request.session['teacher_email']:
            data = notes.objects.filter(teacher_id=request.session['teacher_id'])
            return render (request,'teacher notes.html',{'key':data})
    except :
            return redirect ('home')


def teacher_post_notes(request):
    try:
        if request.session['teacher_email']:
            if request.method == "POST":
                Class = request.POST['Class']
                subject = request.POST['subject']
                file = request.FILES['file']
                data = notes(school_id=request.session['tech_school_id'],teacher_id=request.session['teacher_id'],Class=Class,subject=subject,date=date.today(),name=file.name,file=file)
                data.save()
                return redirect ('teacher/notes')
            return render (request,'teacher post notes.html')
    except :
            return redirect ('home')


def teacher_notice (request):
    try:
        if request.session['teacher_email']:
            if request.method=="POST":
                notice_msg = request.POST['notice_msg']
                data=notice(school_id=request.session['tech_school_id'],teacher_id=request.session['teacher_id'],date=date.today(),notice_msg=notice_msg)
                data.save()
                return redirect ('teacher')
            return render (request,'circulatenotice.html')
    except :
            return redirect ('home')


def teacher_lectures (request):
    try:
        if request.session['teacher_email']:
            if request.method=="POST":
                Class = request.POST['Class']
                subject = request.POST['subject']
                link=request.POST['link']
                data = lectures(school_id=request.session['tech_school_id'],teacher_id=request.session['teacher_id'],Class=Class,subject=subject,link=link)
                data.save()
                return redirect('teacher')
            return render (request,'teachcer lectures.html')
    except :
            return redirect ('home')



def teacher_event (request):
    try:
        if request.session['teacher_email']:
            if request.method=="POST":
                    Class = request.POST['Class']
                    type = request.POST['type']
                    file = request.FILES['file']
                    data = info(school_id=request.session['tech_school_id'],teacher_id=request.session['teacher_id'],Class=Class,type=type,file=file)
                    data.save()
                    return redirect('teacher')
            return render (request,'syllabusreport.html')


    except :
            return redirect ('home')

#------------------------------------------------------------------------------------------------
def delete (request):
    print(request.session['student_email'])
    print(request.session['school_id'])
    print(request.session['Class'])
    return HttpResponse("lol")
'''def upload (request):
    if request.method == "POST"  :

        file = request.FILES['ref']
        fs = FileSystemStorage() #calling file system storage
        name = fs.save(upload.name,upload) # saving it to file
        url = fs.url(name)   # creating url for uploaded image
        return render (request,'upload.html',{'url':url})
    return render (request,'upload.html')



def notebook (request):
    if request.method == "POST":
        form = notebookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('image')
    else:
        form = notebookForm()
    return render (request,'school old/upload.html',{'form':form})'''
def image(request):
    x = date.today()
    return HttpResponse(x)
