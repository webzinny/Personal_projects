from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
import mysql.connector as sql
db = sql.connect(host="localhost",user="atul",password="Password@ibs",db="reports")

def checkConn():
    try:
        cur = db.cursor()
        return True
    except:
        db = sql.connect(host="localhost",user="atul",password="Password@ibs",db="reports")
        return True


def login(request):
    if('admin' in request.session):
        return redirect('admin')
    if('userId' in request.session):
        return redirect('userView')
    return render(request,'login.html')

def validate(request):
    if request.method=="POST":
        email=request.POST['email']
        pas=request.POST['pas']
        if(email=="admin@admin.com" and pas=="admin"):
            request.session['admin']="adminGranted"
            return redirect('admin')
        else:
            try:
                data = user.objects.get(email=email)
                if(data.status):
                    if(data.pas==pas):
                        request.session['userId']=data.id
                        request.session['userEmail']=data.email
                        return redirect('userView')
                    else:
                        return render(request,'login.html',{'msg':'Wrong pass'})
                else:
                    return render(request,'login.html',{'msg':'You are not allowed'})
            except:
                return render(request,'login.html',{'msg':'No user exists'})
    else:
        return redirect('login')

# ---------------------Admin section-----------------------------------------------------------
def adminPanel(request):
    if('admin' in request.session):
        userData=user.objects.all()
        clientData=client.objects.all()
        return render(request,'admin.html',{'userData':userData,'clientData':clientData})
    else:
        return redirect('login')

def createUser(request):
    if('admin' in request.session):
        if(request.method=="POST"):
            name=request.POST['userName']
            email=request.POST['userEmail']
            pas=request.POST['pass']
            status = request.POST.get('status')
            state=request.POST['state']
            reps=request.POST.getlist('rep-select')
            if(status):
                status = True
            else:
                status=False
            d=user(name=name,email=email,pas=pas,status=status)
            d.save()
            reps=list(map(int,reps))
            d.reports.add(*reps)
            d.save()
            if(state=="no"):
                return redirect("admin")
            else:
                return redirect("createUser")
        else:
            data=report.objects.all()
            return render(request,'createUser.html',{'data':data})
    else:
        return redirect('login')

def editUser(request,id):
    if('admin' in request.session):
        obj=user.objects.get(id=id)
        rep=report.objects.all()
        if(request.method=="POST"):
            state=request.POST['state']
            if(state=="yes"):
                obj.delete()
                return redirect('admin')
            else:
                obj.name=request.POST['userName']
                obj.email=request.POST['userEmail']
                obj.pas=request.POST['pass']
                status = request.POST.get('status')
                reps=request.POST.getlist('rep-select')
                reps=list(map(int,reps))
                obj.reports.clear()
                obj.reports.add(*reps)
            if(status):
                obj.status = True
            else:
                obj.status=False
            obj.save()
            return redirect('admin')
        return render(request,'editUser.html',{'user':obj,'rep':rep})
    else:
        return redirect('login')

def createClient(request):
    if('admin' in request.session):
        if(request.method=="POST"):
            name=request.POST['name']
            d=client(name=name)
            d.save()
            return redirect("admin")
        else:
            return render(request,'createClient.html')
    else:
        return redirect('login')

def reportView(request,id):
    if('admin' in request.session):
        cl=client.objects.get(id=id)
        if request.method=="POST":
            cl=client.objects.get(id=id)
            d=report(client=cl,name=request.POST['repName'])
            d.save()

            clmnNames = request.POST.getlist('clmnNames')
            for i in range(len(clmnNames)):
                a=clmnNames[i].split()
                a="_".join(a)
                clmnNames[i]=a

            query = "create table $"+str(d.id)+" ( S_no int PRIMARY KEY AUTO_INCREMENT,User tinytext,Date datetime,"
            query+=" tinytext,".join(clmnNames)
            query+=" tinytext)"

            checkConn()
            curs = db.cursor()
            curs.execute(query)
            curs.close()

        data=report.objects.filter(client=id)
        return render(request,'createReport.html',{'data':data,"cl":cl})
    else:
        return redirect('login')

def insideViewRepo(request,id):
    if('admin' in request.session):
        rep=report.objects.get(id=id)
        checkConn()
        curs = db.cursor()
        curs.execute("select * from $"+str(id))
        return render(request,'viewReport.html',{'curs':curs,'rep':rep})
    else:
        return redirect('login')

def delReport(request,id):
    if('admin' in request.session):
        rep=report.objects.get(id=id)
        rep.delete()
        query="drop table $"+str(id)
        checkConn()
        curs = db.cursor()
        curs.execute(query)
        curs.close()
        return redirect('admin')
    else:
        return redirect('login')

def adminLogOut(request):
    try:
        del request.session['admin']
        return redirect('login')
    except:
        return redirect('login')

#---------------------User section-------------------------------------------------------------
def userView(request):
    if('userId' in request.session):
        use=user.objects.get(id=request.session['userId'])
        rep=use.reports.all()
        return render(request,'userView.html',{"repData":rep,'userData':use})
    else:
        return redirect('login')

def userForm(request,id):
    if('userId' in request.session):
        repo=report.objects.get(id=id)
        checkConn()
        curs = db.cursor()
        curs.execute("show columns from $"+str(id))
        li=[]
        for i in curs:
            li.append(i[0])
        if(request.method=="POST"):
            data = request.POST.getlist('inpData')
            query ="insert into $"+str(id)+" ("+ ",".join(li[1:]) +") values ( '"+request.session['userEmail']+"','"+str(datetime.now())+"',"
            st = "'%s',"*(len(data)-1)
            query+=st+"'%s')"
            checkConn()
            curs = db.cursor()
            curs.execute(query%tuple(data))
            db.commit()
            curs.close()
            return redirect('userView')
        li=li[3:]
        for i in range(len(li)):
            li[i]=li[i].replace("_"," ")
        return render(request,'userForm.html',{'curs':li,'repname':repo.name})
    else:
        return redirect('login')

def userRepoView(request,repId):
    if('userId' in request.session):
        use=user.objects.get(id=request.session['userId'])
        query = "select * from $"+str(repId)+" where User = '%s'" %str(use.email)
        checkConn()
        curs = db.cursor()
        curs.execute(query)
        return render(request,'userRepView.html',{'curs':curs})
    else:
        return redirect('login')


def userLogOut(request):
    try:
        del request.session['userId']
        del request.session['userEmail']
        return redirect('login')
    except Exception as e:
        return redirect('login')
