from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *


def home(request):
    data = categoryContent.objects.all()
    return render(request,'index.html',{'data':data})

def adminLogin(request):
    if 'passKey' in request.session:
        return redirect(adminDashboard)
    if request.method=='POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        if (user=='admin' ) and (password=='admin'):
            request.session['passKey']="dbfair"
            return redirect(adminDashboard)
        else:
            return render(request,'adminLogin.html',{'msg':"Wrong credentials"})
    return render(request,'adminLogin.html')

def adminDashboard(request):
    if 'passKey' in request.session:
        if request.method=='POST':
            tag = request.POST['tag']
            description = request.POST['description']
            img = request.FILES['img']
            data = categoryContent(tag=tag,description=description,img=img)
            data.save()
        return render(request,'adminDashboard.html')
    else:
        return redirect(adminLogin)

def adminContent(request):
    data = categoryContent.objects.all()
    json = {}
    count = 1
    for i in data:
        json.update({count:{'tag':i.tag,'desc':i.description ,'img':i.img.url}})
        count+=1
    return JsonResponse(json)

def adminLogOut(request):
    del request.session['passKey']
    return redirect(adminLogin)
