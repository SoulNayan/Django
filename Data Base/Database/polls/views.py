from django.shortcuts import render,HttpResponse,redirect
from polls.models import Question

def Home(request):
   all=Question.objects.all()
   return render(request,'Data.html',{"all":all})

def creat(request):
    id=request.GET.get('id')
    print("idd",id)
    name1=request.GET.get('name')
    surname=request.GET.get('surname')
    if id:
        Question.objects.filter(id=id).update(name=name1,surname=surname)
    else:
        Question.objects.create(name=name1,surname=surname)
    return redirect("/")

def delete(request):
    id=request.GET.get('deleteid')
    fillter=Question.objects.filter(id=id).first()
    fillter.delete()
    return redirect("/")

def Edit(request):
    edit=request.GET.get('Editid')
    print("edit",edit)
    id=Question.objects.filter(id=edit).first()
    print("id",id)
    return render(request,'Data.html',{"id":id})

