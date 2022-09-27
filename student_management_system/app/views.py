from django.shortcuts import render
from .models import studentDetails
from .forms import studentDetailsForms
from django.http import HttpResponseRedirect
# Create your views here.
def base(request):
    return render(request,'app/base.html')

def studentDetails_show(request):
    if request.method=='POST':
        fm=studentDetailsForms(request.POST)
        if fm.is_valid():
            fm.save()
            fm=studentDetailsForms()
    else:
       fm=studentDetailsForms()
    stud=studentDetails.objects.all()
    return render(request,'app/base.html',{'form':fm,'stu':stud})

def update_data(request,id):
    if request.method=='POST':
        pi=studentDetails.objects.get(pk=id)
        fm=studentDetailsForms(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=studentDetails.objects.get(pk=id)
        fm=studentDetailsForms(instance=pi)
    return render(request,'app/base.html',{'form':fm})

def delete_data(request,id):
   if request.method=='POST':
    pi=studentDetails.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/')

def home(request):
    return render(request,'app/home.html')

def instutions(request):
    return render(request,'app/instutions.html')

def administration(request):
    return render(request,'app/administration.html')

def department(request):
    return render(request,'app/department.html')

def contact(request):
    return render(request,'app/contact.html')

def course(request):
    return render(request,'app/courses.html')

def library(request):
    return render(request,'app/library.html')

def placementCell(request):
    return render(request,'app/placementCell.html')

def adminisons(request):
    return render(request,'app/adminisons.html')

def chairman(request):
    return render(request,'app/chairman.html')

def md(request):
    return render(request,'app/md.html')