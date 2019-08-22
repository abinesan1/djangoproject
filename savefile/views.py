from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.


from .models import FileDetails
from django.shortcuts import render  
from django.http import HttpResponse  
from .functions import handle_uploaded_file  
from .forms import StudentForm  ,AdminLogin
from os.path import splitext



import os



def loginadmin(request):  
    if request.method == 'POST':  
        username=request.POST.get('username')
        password= request.POST.get('password')
        if username=="admin" and password=="123456":
           Alldetail = FileDetails.objects.filter(status='underreview')  
           return render(request,"show.html",{'detail':Alldetail}) 
        else:
           return HttpResponse("Please provide vaild credentials to login")
    else:
        admin = AdminLogin()  
        return render(request,'admin.html',{'form':admin})
           

def viewfiles(request,path):
    if 1:
        print("::::::::::::::::::::",path)
        os.startfile(''+path)
        Alldetail = FileDetails.objects.filter(status='underreview')  
        return render(request,"show.html",{'detail':Alldetail})
          
    else:
        print("::::::::::::::::::::",path)
        Alldetail = FileDetails.objects.filter(status='underreview')  
        return render(request,"show.html",{'detail':Alldetail})

def userapplication(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)
        emails=request.POST.get('email')  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'],emails)
            e=request.FILES['file']
            file_name,extension = splitext(e.name)
    
            
            
            post=FileDetails()
            post.firstname = request.POST.get('firstname')
            post.lastname  = request.POST.get('lastname')
            post.email =request.POST.get('email')
            url=request.POST.get('email')+extension
          
            post.status='underreview'
            post.mobilenum =request.POST.get('mobilenumber')
            post.fileurl =url
            
             
            post.save()
            return HttpResponse("Application submitted successfuly ")  
    else:  
        student = StudentForm()  
        return render(request,'index.html',{'form':student})  



def show(request):  
    Alldetail = FileDetails.objects.filter(status='underreview')  
    return render(request,"show.html",{'detail':Alldetail}) 


def update(request, id):  
    updt= FileDetails.objects.get(id=id)  
    updt.status='approved'
    updt.save()
    Alldetail = FileDetails.objects.filter(status='approved') 
    return render(request,"show.html",{'detail':Alldetail}) 


def selectedlist(request):
   
    Alldetail = FileDetails.objects.filter(status='approved')  
    return render(request,"showselected.html",{'detail':Alldetail}) 


def rejectedlist(request):
   
    Alldetail = FileDetails.objects.filter(status='rejected')  
    return render(request,"showdeleted.html",{'detail':Alldetail}) 

def reject(request, id):  
    updt= FileDetails.objects.get(id=id)
    updt.status='rejected'
    updt.save()
    
    Alldetail = FileDetails.objects.filter(status='rejected')  
    return render(request,"showdeleted.html",{'detail':Alldetail}) 

    
     
