from django.shortcuts import render,redirect
from .models import Data
# Create your views here.
def home(request):
    data=Data.objects.all()
    context={
        'data':data
    }
    return render(request,'index.html',context)
def forms(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        reg=Data(name=name,address=address,phone=phone)
        reg.save()
        return redirect("home")
    return render(request,'from.html')
def delete_d(request,id):
    data=Data.objects.get(id=id)
    data.delete()
    return redirect("home")
def edit(request,id):
    data=Data.objects.get(id=id)
    context={
        'data':data

    }
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        phone=request.POST['phone']
        reg=Data.objects.get(id=id)
        reg.name=name
        reg.address=address
        reg.phone=phone
        reg.save()
        return redirect("home")
    return render(request,"edit.html",context)