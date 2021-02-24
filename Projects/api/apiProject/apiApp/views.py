from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import student
from django.views.decorators.csrf import csrf_exempt
from .serializer import studentSerializer

def test(request):
    return render(request,'test.html')

def validate(request):
    email=request.GET['email']
    pas=request.GET['pas']
    try:
        user=student.objects.get(email=email)
        if pas == user.pas:
            return JsonResponse({'status':'ok','id':user.id})
        else:
            return JsonResponse({'status':'Wrong pass'})
    except Exception as e:
        return JsonResponse({'status':'No user Found'})

@csrf_exempt
def getData(request):
    if request.method=="GET":
        data=student.objects.all()
        data=studentSerializer(data,many=True)
        print(data.data)
        return JsonResponse(data.data,safe=False)

def studentData(request,id):
    user=student.objects.get(id=id)
    return JsonResponse(
    {'id':user.id,'Name':user.Name,'email':user.email,'pas':user.pas,"clas": user.clas, "sub1": user.sub1, "sub2": user.sub2, "sub3": user.sub3, "sub4": user.sub4, "sub5": user.sub5, "sports": user.sports}
    )
