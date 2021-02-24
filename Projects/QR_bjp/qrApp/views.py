from django.shortcuts import render,redirect
from .models import BJPdata

def scanner(request):
    if request.method=="POST":
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        selectInp = request.POST['selectInp']
        data = BJPdata(Designation=input1,Name=input2,Place=input3,Contact=input4,Sess=selectInp)
        data.save()
        return redirect('success')
    return render(request,"qrMain.html")

def success(request):
    return render(request,"qrMain.html",{'msg':'Submitted'})

def login(request):
    if 'admin' in request.session:
        return redirect('admin')
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pass']
        if(email=="admin@admin.com" and pas=="admin"):
            request.session['admin']='admin'
            return redirect('admin')
        else:
            return render(request,'login.html',{"msg":"Wrong credential's"})
    return render(request,'login.html')

def admin(request):
    if 'admin' in request.session:
        data = BJPdata.objects.all()
        return render(request,'admin.html',{'data':data})
    else:
        return redirect('login')

def logout(request):
    try:
        del request.session['admin']
        return redirect("login")
    except Exception as e:
        return redirect("login")

def dbEmpty(request):
    if request.method=="POST":
        pas=request.POST['pas']
        if pas=="empty":
            data = BJPdata.objects.all().delete()
            return render(request,"dbAdmin.html",{"msg":"Success"})
        else:
            return render(request,"dbAdmin.html",{"msg":"Wrong Pass"})
    return render(request,"dbAdmin.html")
