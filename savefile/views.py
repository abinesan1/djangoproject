from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.core.mail import send_mail
from django.conf import settings
from .models import FileDetails
from django.shortcuts import render  
from django.http import HttpResponse  
from .functions import handle_uploaded_file  
from .forms import StudentForm  
from os.path import splitext



import os


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


             
            subject = "APPLICATION"
            message = "we recevied your appilication once shortlisted we will get you back soon"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [emails,]
            send_mail( subject, message, email_from, recipient_list ) 
            return HttpResponse("Application submitted successfuly after the selection process we will update you the status on mail.kindly check the mail ")  
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
    
    
    subject = "APPLICATION STATUS"
    message = "congratulation Your application selected"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [updt.email,]
    send_mail( subject, message, email_from, recipient_list )
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
   
    subject = "APPLICATION STATUS"
    message = "Your application was not shortlisted"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [updt.email,]
    send_mail( subject, message, email_from, recipient_list ) 
    
    Alldetail = FileDetails.objects.filter(status='rejected')  
    return render(request,"showdeleted.html",{'detail':Alldetail}) 

    
     