from django import forms  
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)
    lastname  = forms.CharField(label="Enter last name", max_length = 10)  
    mobilenumber  = forms.CharField(label="mobile number", max_length = 20)
    email     = forms.EmailField(label="Enter Email")  
    file      = forms.FileField() # for creating file input
    print(firstname,lastname,email)
   

class AdminLogin(forms.Form):  
    username     = forms.CharField(label="Enter user name")
    password  = forms.CharField(label="Password", max_length = 20) 
    print(password,username)
