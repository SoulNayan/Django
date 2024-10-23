from django.shortcuts import render,HttpResponse,redirect
from polls.models import Question

# def Home(self):
#     return render(self,'Result.html')
# def get(self):
#     name=self.GET.get('username')
#     subM=self.GET.get('sub1'),self.GET.get('sub2'),self.GET.get('sub3'),self.GET.get('sub4'),self.GET.get('sub5'),self.GET.get('sub6') #we get all value in string and will be stored in tuple
#     subM=list(subM) #To convert Tuple to list
#     subMT=[]
 
#     for i in subM:  #To convert all str variable in main list to int 
#             subMT.append(int(i))
#     Total=sum(subMT)
#     b=["FAIL","PASS",40,Total//6]
#     subR=[]
#     for i in range(0,len(subM)):
#         if subMT[i]<b[2]:
#             subR.append(b[0])
#         else:
#             subR.append(b[1])
#     return render(self,'Result.html',{
#         'Name':name,
#         'sub1M':subM[0],
#         'sub2M':subM[1],
#         'sub3M':subM[2],
#         'sub4M':subM[3],
#         'sub5M':subM[4],
#         'sub6M':subM[5],
#         'subR1':subR[0],
#         'subR2':subR[1],
#         'subR3':subR[2],
#         'subR4':subR[3],
#         'subR5':subR[4],
#         'subR6':subR[5],
#         'Total':Total,
#         'Min':b[2],
#         'Percentage':b[3]
#     })

def Home(request):
    all=Question.objects.all()
    return render(request,'creat.html',{"all":all})

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
def delet(request):
    id=request.GET.get('deleteid')
    fill=Question.objects.filter(id=id).first()
    fill.delete()
    return redirect("/")
def edit(request):
    edit=request.GET.get('Editid')
    print("edit",edit)
    id=Question.objects.filter(id=edit).first()
    print("id",id)
    return render(request,'creat.html',{"id":id})